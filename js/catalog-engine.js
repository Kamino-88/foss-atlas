/* FOSS Atlas catalog engine v1
 * Conservative deduplication: IDs and normalized names are deduplicated automatically.
 * Shared official-site hosts are reported as review candidates, never auto-merged.
 */
(function (global) {
  "use strict";
  function normalizeName(value) {
    return String(value || "").normalize("NFKD").toLowerCase()
      .replace(/[™®©]/g, "").replace(/[^a-z0-9]+/g, " ").trim()
      .replace(/\b(software|application|app|project)\b/g, "").replace(/\s+/g, " ").trim();
  }
  function hostOf(value) {
    try { return new URL(value).hostname.toLowerCase().replace(/^www\./, ""); }
    catch (_) { return ""; }
  }
  function uniqueRecords(records, options) {
    const opts = options || {};
    const seenIds = new Set(), seenNames = new Set(), result = [], audit = [];
    (Array.isArray(records) ? records : []).forEach(function (record) {
      if (!record || !record.id || !record.name) {
        audit.push({ type: "invalid-record", id: record && record.id || "", name: record && record.name || "" });
        return;
      }
      if (opts.requireOpenSource && record.open_source !== true) {
        audit.push({ type: "not-confirmed-open-source", id: record.id, name: record.name });
        return;
      }
      if (opts.requireFreeToUse && record.free_to_use !== true) {
        audit.push({ type: "free-to-use-not-confirmed", id: record.id, name: record.name });
        return;
      }
      const id = String(record.id).trim().toLowerCase();
      const name = normalizeName(record.name);
      if (seenIds.has(id)) {
        audit.push({ type: "duplicate-id", id: record.id, name: record.name });
        return;
      }
      if (name && seenNames.has(name)) {
        audit.push({ type: "duplicate-normalized-name", id: record.id, name: record.name });
        return;
      }
      seenIds.add(id);
      if (name) seenNames.add(name);
      result.push(record);
    });
    return { records: result, audit: audit };
  }
  function reviewSharedHosts(records) {
    const hosts = new Map();
    (records || []).forEach(function (record) {
      const host = hostOf(record && record.official_website);
      if (!host) return;
      if (!hosts.has(host)) hosts.set(host, []);
      hosts.get(host).push({ id: record.id, name: record.name });
    });
    return Array.from(hosts.entries())
      .filter(function (entry) { return entry[1].length > 1; })
      .map(function (entry) { return { type: "shared-official-host-review", host: entry[0], projects: entry[1] }; });
  }
  global.FOSSCatalogEngine = {
    normalizeName: normalizeName,
    hostOf: hostOf,
    uniqueRecords: uniqueRecords,
    reviewSharedHosts: reviewSharedHosts
  };
})(window);
