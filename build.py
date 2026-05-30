#!/usr/bin/env python3
"""Build the SMGTEC Proposal Generator HTML file."""
import os

path = "/home/alpha/Proposals/calculator/index.html"

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SMGTEC Proposal Generator</title>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NH9SQDQM');</script>
<!-- End Google Tag Manager -->
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #0a0a0a;
  --bg-elevated: #111111;
  --bg-card: #161616;
  --bg-input: #1a1a1a;
  --bg-input-focus: #222222;
  --gold: #DEDBC8;
  --gold-dim: rgba(222, 219, 200, 0.15);
  --gold-mid: rgba(222, 219, 200, 0.5);
  --text: #e8e8e8;
  --text-dim: #888888;
  --text-muted: #555555;
  --accent: #c4a35a;
  --danger: #dc3545;
  --danger-bg: rgba(220, 53, 69, 0.1);
  --danger-border: rgba(220, 53, 69, 0.3);
  --success: #28a745;
  --border: rgba(255,255,255,0.06);
  --border-bright: rgba(222, 219, 200, 0.2);
  --radius: 8px;
  --radius-lg: 12px;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Inter', sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4, .logo-text, .cover-title, .cover-subtitle, .tier-name {
  font-family: 'Instrument Serif', serif;
}

/* Header */
.header {
  background: var(--bg-elevated);
  border-bottom: 1px solid var(--border);
  padding: 0 24px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
}
.logo { display: flex; align-items: center; gap: 10px; }
.logo-mark {
  width: 32px; height: 32px;
  background: linear-gradient(135deg, var(--gold), var(--accent));
  border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Instrument Serif', serif; font-weight: 700;
  color: var(--bg); font-size: 16px;
}
.logo-text { color: var(--gold); font-size: 18px; letter-spacing: 1px; }
.header-actions { display: flex; align-items: center; gap: 12px; }

.lang-toggle {
  display: flex; background: var(--bg-input); border-radius: 6px;
  border: 1px solid var(--border); overflow: hidden;
}
.lang-btn {
  padding: 6px 14px; font-size: 12px; font-weight: 600;
  background: transparent; color: var(--text-dim); border: none;
  cursor: pointer; transition: all 0.2s; font-family: 'Inter', sans-serif;
}
.lang-btn.active { background: var(--gold); color: var(--bg); }
.lang-btn:hover:not(.active) { color: var(--gold); }

.view-toggle {
  display: flex; background: var(--bg-input); border-radius: 6px;
  border: 1px solid var(--border); overflow: hidden;
}
.view-btn {
  padding: 6px 14px; font-size: 12px; font-weight: 600;
  background: transparent; color: var(--text-dim); border: none;
  cursor: pointer; transition: all 0.2s; font-family: 'Inter', sans-serif;
}
.view-btn.active { background: var(--gold); color: var(--bg); }
.view-btn:hover:not(.active) { color: var(--gold); }

/* Layout */
.layout {
  display: grid;
  grid-template-columns: 340px 1fr;
  min-height: calc(100vh - 56px);
}

/* Sidebar */
.sidebar {
  background: var(--bg-elevated);
  border-right: 1px solid var(--border);
  padding: 24px;
  overflow-y: auto;
  max-height: calc(100vh - 56px);
  position: sticky;
  top: 56px;
}
.sidebar-title {
  font-family: 'Instrument Serif', serif;
  color: var(--gold); font-size: 20px; margin-bottom: 20px;
  letter-spacing: 0.5px;
}

.form-group { margin-bottom: 16px; }
.form-label {
  display: block; font-size: 11px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 1px;
  color: var(--text-dim); margin-bottom: 6px;
}
.form-input, .form-select {
  width: 100%; padding: 10px 12px;
  background: var(--bg-input); border: 1px solid var(--border);
  border-radius: var(--radius); color: var(--text);
  font-family: 'Inter', sans-serif; font-size: 14px;
  transition: border-color 0.2s;
}
.form-input:focus, .form-select:focus {
  outline: none; border-color: var(--gold-mid);
  background: var(--bg-input-focus);
}
.form-select { appearance: none; cursor: pointer; }
.form-select option { background: var(--bg-input); color: var(--text); }

/* Number inputs */
.number-input-wrap {
  display: flex; align-items: center; gap: 8px;
}
.num-btn {
  width: 32px; height: 36px;
  background: var(--bg-input); border: 1px solid var(--border);
  border-radius: var(--radius); color: var(--gold);
  font-size: 18px; cursor: pointer; display: flex;
  align-items: center; justify-content: center;
  transition: all 0.2s; flex-shrink: 0;
}
.num-btn:hover { background: var(--gold-dim); border-color: var(--gold-mid); }
.num-input {
  width: 60px; text-align: center; padding: 8px;
  background: var(--bg-input); border: 1px solid var(--border);
  border-radius: var(--radius); color: var(--text);
  font-family: 'Inter', sans-serif; font-size: 16px; font-weight: 600;
  -moz-appearance: textfield;
}
.num-input::-webkit-inner-spin-button, .num-input::-webkit-outer-spin-button { -webkit-appearance: none; }
.num-input:focus { outline: none; border-color: var(--gold-mid); }
.num-label { font-size: 13px; color: var(--text-dim); }

/* Scrape field */
.scrape-wrap { position: relative; }
.scrape-indicator {
  position: absolute; right: 10px; top: 50%; transform: translateY(-50%);
  font-size: 11px; font-weight: 600;
}
.scrape-indicator.loading { color: var(--accent); }
.scrape-indicator.success { color: var(--success); }
.scrape-indicator.error { color: var(--danger); }

/* Budget range */
.budget-options { display: flex; gap: 8px; }
.budget-btn {
  flex: 1; padding: 8px; text-align: center;
  background: var(--bg-input); border: 1px solid var(--border);
  border-radius: var(--radius); cursor: pointer;
  font-size: 12px; font-weight: 500;
  transition: all 0.2s; color: var(--text-dim);
}
.budget-btn.active { border-color: var(--gold); background: var(--gold-dim); color: var(--gold); }
.budget-btn:hover:not(.active) { border-color: var(--gold-mid); }

/* Add-on checkboxes */
.addon-group { display: flex; flex-direction: column; gap: 8px; }
.addon-item {
  display: flex; align-items: center; gap: 10px;
  cursor: pointer; font-size: 13px; color: var(--text-dim);
}
.addon-item input[type="checkbox"] {
  width: 16px; height: 16px; accent-color: var(--accent);
  cursor: pointer;
}

/* Generate button */
.btn-generate {
  width: 100%; padding: 14px;
  background: linear-gradient(135deg, var(--gold), var(--accent));
  border: none; border-radius: var(--radius);
  color: var(--bg); font-family: 'Inter', sans-serif;
  font-size: 15px; font-weight: 700; letter-spacing: 0.5px;
  cursor: pointer; transition: all 0.3s;
  margin-top: 8px;
}
.btn-generate:hover { transform: translateY(-1px); box-shadow: 0 4px 20px rgba(222, 219, 200, 0.2); }
.btn-generate:disabled { opacity: 0.5; cursor: not-allowed; transform: none; box-shadow: none; }

/* Preview area */
.preview {
  padding: 32px;
  overflow-y: auto;
  max-height: calc(100vh - 56px);
  background: var(--bg);
}
.preview-empty {
  display: flex; flex-direction: column; align-items: center;
  justify-content: center; height: 100%; min-height: 400px;
  color: var(--text-muted); text-align: center;
}
.preview-empty-icon { font-size: 48px; margin-bottom: 16px; opacity: 0.3; }

/* Proposal pages */
.proposal-page {
  background: #ffffff;
  color: #1a1a1a;
  max-width: 850px;
  margin: 0 auto 24px;
  padding: 60px 56px;
  border-radius: var(--radius-lg);
  box-shadow: 0 2px 20px rgba(0,0,0,0.3);
  page-break-after: always;
  position: relative;
  overflow: hidden;
}
.proposal-page::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--gold), var(--accent), var(--gold));
}

/* Cover page */
.cover-page { text-align: center; padding-top: 100px; padding-bottom: 100px; }
.cover-logo {
  width: 64px; height: 64px;
  background: linear-gradient(135deg, var(--gold), var(--accent));
  border-radius: 12px;
  display: inline-flex; align-items: center; justify-content: center;
  font-family: 'Instrument Serif', serif; font-weight: 700;
  color: #0a0a0a; font-size: 28px; margin-bottom: 32px;
}
.cover-title { font-size: 36px; color: #1a1a1a; margin-bottom: 8px; letter-spacing: 2px; }
.cover-subtitle { font-size: 18px; color: #888; margin-bottom: 48px; font-style: italic; }
.cover-company {
  font-size: 28px; color: var(--accent); margin-bottom: 16px;
  font-family: 'Instrument Serif', serif; border-bottom: 2px solid var(--gold-dim);
  display: inline-block; padding-bottom: 8px;
}
.cover-contact { font-size: 16px; color: #666; margin-bottom: 4px; }
.cover-meta { font-size: 14px; color: #999; margin-bottom: 8px; }
.cover-valid {
  display: inline-block; margin-top: 48px; padding: 10px 24px;
  border: 2px solid var(--accent); border-radius: 6px;
  color: var(--accent); font-weight: 600; font-size: 14px;
  letter-spacing: 1px;
}

/* Page header */
.page-header {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 32px; padding-bottom: 16px;
  border-bottom: 2px solid var(--gold);
}
.page-header h2 { font-size: 24px; color: #1a1a1a; }
.page-header .smgtec-watermark { font-size: 12px; color: #ccc; font-weight: 600; letter-spacing: 2px; }

/* Executive summary */
.exec-summary { margin-bottom: 32px; }
.exec-summary p { font-size: 15px; color: #444; line-height: 1.8; margin-bottom: 16px; }
.exec-summary strong { color: #1a1a1a; }
.exec-badge {
  display: inline-block; padding: 4px 12px;
  background: var(--gold-dim); border-radius: 4px;
  font-size: 12px; font-weight: 600; color: #8a7030;
  margin-right: 6px; margin-bottom: 6px;
}

/* Risk assessment */
.risk-box {
  border: 1px solid var(--danger-border);
  border-left: 4px solid var(--danger);
  border-radius: var(--radius);
  background: var(--danger-bg);
  padding: 20px 24px; margin-bottom: 24px;
}
.risk-box h3 { font-family: 'Instrument Serif', serif; color: var(--danger); font-size: 18px; margin-bottom: 12px; }
.risk-item { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 8px; font-size: 14px; color: #444; }
.risk-icon { color: var(--danger); flex-shrink: 0; margin-top: 2px; }

/* Tier cards */
.tier-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 32px; }
.tier-card {
  border: 2px solid #e0e0e0;
  border-radius: var(--radius-lg);
  padding: 28px 24px;
  position: relative;
  transition: all 0.3s;
}
.tier-card.recommended {
  border-color: var(--accent);
  box-shadow: 0 0 0 2px rgba(196, 163, 90, 0.2);
  transform: scale(1.02);
}
.tier-card.recommended::after {
  content: attr(data-badge);
  position: absolute; top: -12px; left: 50%; transform: translateX(-50%);
  background: linear-gradient(135deg, var(--gold), var(--accent));
  color: #0a0a0a;
  padding: 4px 16px; border-radius: 20px;
  font-size: 11px; font-weight: 700; letter-spacing: 1px;
  white-space: nowrap;
}
.tier-card.not-recommended { opacity: 0.7; }
.tier-name { font-size: 20px; color: #1a1a1a; margin-bottom: 4px; }
.tier-price { font-size: 32px; font-weight: 700; color: #1a1a1a; margin: 12px 0 4px; }
.tier-price span { font-size: 14px; font-weight: 400; color: #888; }
.tier-onetime { font-size: 13px; color: #666; margin-bottom: 20px; }
.tier-features { list-style: none; padding: 0; }
.tier-features li {
  padding: 6px 0; font-size: 13px; color: #444;
  display: flex; align-items: flex-start; gap: 8px;
  border-bottom: 1px solid #f0f0f0;
}
.tier-features li:last-child { border-bottom: none; }
.tier-check { color: var(--success); flex-shrink: 0; font-weight: 700; }
.tier-cross { color: #ccc; flex-shrink: 0; }

/* Comparison table */
.comparison-table-wrap { overflow-x: auto; margin-bottom: 32px; }
.comparison-table {
  width: 100%; border-collapse: collapse; font-size: 13px;
}
.comparison-table th {
  background: #1a1a1a; color: var(--gold);
  padding: 12px 16px; text-align: left;
  font-weight: 600; letter-spacing: 0.5px;
  font-family: 'Instrument Serif', serif; font-size: 16px;
}
.comparison-table th:first-child { border-radius: 6px 0 0 0; }
.comparison-table th:last-child { border-radius: 0 6px 0 0; }
.comparison-table th:nth-child(3) {
  background: linear-gradient(135deg, #2a2a2a, #1a1a1a);
  position: relative;
}
.comparison-table td {
  padding: 10px 16px; border-bottom: 1px solid #f0f0f0; color: #444;
  text-align: center;
}
.comparison-table td:first-child { text-align: left; font-weight: 500; color: #333; }
.comparison-table tr:nth-child(even) td { background: #fafafa; }
.comparison-table tr:hover td { background: var(--gold-dim); }
.comp-check { color: var(--success); font-weight: 700; font-size: 16px; }
.comp-cross { color: #ccc; }
.comp-partial { color: var(--accent); font-weight: 700; }

/* ROI section */
.roi-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 32px; }
.roi-card {
  border-radius: var(--radius-lg); padding: 28px;
  border: 1px solid;
}
.roi-without { border-color: var(--danger-border); background: var(--danger-bg); }
.roi-with { border-color: rgba(40, 167, 69, 0.3); background: rgba(40, 167, 69, 0.05); }
.roi-card h3 {
  font-family: 'Instrument Serif', serif; font-size: 20px;
  margin-bottom: 16px;
}
.roi-without h3 { color: var(--danger); }
.roi-with h3 { color: var(--success); }
.roi-stat { display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 14px; }
.roi-stat-label { color: #666; }
.roi-stat-value { font-weight: 600; }
.roi-without .roi-stat-value { color: var(--danger); }
.roi-with .roi-stat-value { color: var(--success); }

/* Addons section */
.addons-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 32px; }
.addon-card {
  border: 1px solid #e0e0e0; border-radius: var(--radius);
  padding: 20px;
}
.addon-card h4 { font-size: 16px; color: #1a1a1a; margin-bottom: 8px; }
.addon-card p { font-size: 13px; color: #666; margin-bottom: 8px; }
.addon-price { font-size: 14px; font-weight: 600; color: var(--accent); }

/* Internal section */
.internal-section {
  background: #f8f8f8;
  border: 2px dashed #ccc;
  border-radius: var(--radius);
  padding: 24px;
  margin-bottom: 24px;
}
.internal-section h3 {
  font-family: 'Instrument Serif', serif;
  font-size: 18px; color: var(--danger); margin-bottom: 16px;
}
.internal-table { width: 100%; border-collapse: collapse; font-size: 13px; margin-bottom: 16px; }
.internal-table th { background: #eee; padding: 8px 12px; text-align: left; font-weight: 600; color: #333; }
.internal-table td { padding: 8px 12px; border-bottom: 1px solid #eee; color: #444; }
.internal-table .right { text-align: right; }
.internal-total { font-weight: 700; color: #1a1a1a; background: #f0f0f0; }
.internal-margin { color: var(--success); font-weight: 600; }
.internal-margin-low { color: var(--danger); font-weight: 600; }

/* Objection handling */
.objection-item {
  background: #fff; border: 1px solid #e0e0e0;
  border-radius: var(--radius); padding: 16px; margin-bottom: 12px;
}
.objection-q { font-weight: 600; color: #1a1a1a; margin-bottom: 6px; font-size: 14px; }
.objection-a { color: #666; font-size: 13px; }

/* Engineer workflow */
.workflow-steps { counter-reset: step; list-style: none; padding: 0; }
.workflow-steps li {
  counter-increment: step;
  position: relative; padding: 0 0 20px 40px;
  font-size: 14px; color: #444;
}
.workflow-steps li::before {
  content: counter(step);
  position: absolute; left: 0; top: 0;
  width: 28px; height: 28px;
  background: linear-gradient(135deg, var(--gold), var(--accent));
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #0a0a0a; font-weight: 700; font-size: 13px;
}
.workflow-steps li::after {
  content: '';
  position: absolute; left: 13px; top: 32px; bottom: 0;
  width: 2px; background: #e0e0e0;
}
.workflow-steps li:last-child::after { display: none; }

/* Next step page */
.next-step-page { text-align: center; padding: 80px 56px; }
.next-step-page h2 { font-size: 32px; color: #1a1a1a; margin-bottom: 16px; }
.next-step-page p { font-size: 16px; color: #666; margin-bottom: 32px; }
.btn-print {
  display: inline-block; padding: 14px 32px;
  background: linear-gradient(135deg, var(--gold), var(--accent));
  border: none; border-radius: 8px;
  color: #0a0a0a; font-family: 'Inter', sans-serif;
  font-size: 15px; font-weight: 700; letter-spacing: 0.5px;
  cursor: pointer; transition: all 0.3s; text-decoration: none;
}
.btn-print:hover { transform: translateY(-2px); box-shadow: 0 4px 20px rgba(222, 219, 200, 0.3); }

/* Section divider */
.section-title {
  font-family: 'Instrument Serif', serif;
  font-size: 22px; color: #1a1a1a;
  margin: 32px 0 20px;
  padding-bottom: 8px;
  border-bottom: 2px solid var(--gold);
}

/* Mobile responsive */
@media (max-width: 1024px) {
  .tier-cards { grid-template-columns: 1fr; }
  .roi-grid { grid-template-columns: 1fr; }
  .addons-grid { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { max-height: none; position: static; border-right: none; border-bottom: 1px solid var(--border); }
  .preview { padding: 16px; }
  .proposal-page { padding: 32px 24px; }
  .cover-page { padding-top: 60px; padding-bottom: 60px; }
  .cover-title { font-size: 28px; }
  .tier-cards { grid-template-columns: 1fr; }
  .comparison-table { font-size: 11px; }
  .comparison-table th, .comparison-table td { padding: 8px 10px; }
  .header { padding: 0 16px; }
  .logo-text { font-size: 14px; }
}

/* Print styles */
@media print {
  .header, .sidebar, .btn-print, .internal-section { display: none !important; }
  .layout { display: block; }
  .preview { padding: 0; max-height: none; overflow: visible; }
  .proposal-page { box-shadow: none; border-radius: 0; margin: 0; padding: 40px; page-break-after: always; }
}
</style>
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NH9SQDQM"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<div class="header">
  <div class="logo">
    <div class="logo-mark">S</div>
    <span class="logo-text">SMGTEC</span>
  </div>
  <div class="header-actions">
    <div class="view-toggle">
      <button class="view-btn active" data-view="client" id="btn-view-client">Client</button>
      <button class="view-btn" data-view="internal" id="btn-view-internal">Internal</button>
    </div>
    <div class="lang-toggle">
      <button class="lang-btn active" data-lang="en" id="btn-lang-en">EN</button>
      <button class="lang-btn" data-lang="es" id="btn-lang-es">ES</button>
    </div>
  </div>
</div>

<div class="layout">
  <!-- Sidebar Form -->
  <div class="sidebar">
    <div class="sidebar-title" data-i18n="form_title">Proposal Configuration</div>
    
    <div class="form-group">
      <label class="form-label" data-i18n="company_name">Company Name</label>
      <input type="text" class="form-input" id="companyName" placeholder="Acme Industries">
    </div>
    
    <div class="form-group">
      <label class="form-label" data-i18n="website">Website</label>
      <div class="scrape-wrap">
        <input type="text" class="form-input" id="website" placeholder="https://example.com">
        <span class="scrape-indicator" id="scrapeIndicator"></span>
      </div>
    </div>
    
    <div class="form-group">
      <label class="form-label" data-i18n="contact_name">Contact Name</label>
      <input type="text" class="formInput" id="contactName" placeholder="John Smith">
    </div>
    
    <div class="form-group">
      <label class="form-label" data-i18n="industry">Industry</label>
      <select class="form-select" id="industry">
        <option value="legal" data-i18n="ind_legal">Legal</option>
        <option value="healthcare" data-i18n="ind_healthcare">Healthcare</option>
        <option value="finance" data-i18n="ind_finance">Finance</option>
        <option value="retail" data-i18n="ind_retail">Retail</option>
        <option value="manufacturing" data-i18n="ind_manufacturing">Manufacturing</option>
        <option value="other" data-i18n="ind_other">Other</option>
      </select>
    </div>
    
    <div class="form-group">
      <label class="form-label" data-i18n="location">Location</label>
      <select class="form-select" id="location">
        <option value="spain" data-i18n="loc_spain">Spain</option>
        <option value="eu" data-i18n="loc_eu">European Union</option>
        <option value="other" data-i18n="loc_other">Other</option>
      </select>
    </div>
    
    <div class="form-group">
      <label class="form-label" data-i18n="devices">Devices</label>
      <div class="number-input-wrap" style="margin-bottom:8px;">
        <button class="num-btn" onclick="adjustNum('workstations',-1)">−</button>
        <input type="number" class="num-input" id="workstations" value="5" min="0" max="500">
        <button class="num-btn" onclick="adjustNum('workstations',1)">+</button>
        <span class="num-label" data-i18n="workstations">Workstations</span>
      </div>
      <div class="number-input-wrap" style="margin-bottom:8px;">
        <button class="num-btn" onclick="adjustNum('laptops',-1)">−</button>
        <input type="number" class="num-input" id="laptops" value="2" min="0" max="500">
        <button class="num-btn" onclick="adjustNum('laptops',1)">+</button>
        <span class="num-label" data-i18n="laptops">Laptops</span>
      </div>
      <div class="number-input-wrap">
        <button class="num-btn" onclick="adjustNum('servers',-1)">−</button>
        <input type="number" class="num-input" id="servers" value="0" min="0" max="50">
        <button class="num-btn" onclick="adjustNum('servers',1)">+</button>
        <span class="num-label" data-i18n="servers">Existing Servers</span>
      </div>
    </div>
    
    <div class="form-group">
      <label class="form-label" data-i18n="current_it">Current IT State</label>
      <select class="form-select" id="emailProvider" style="margin-bottom:8px;">
        <option value="none" data-i18n="email_none">No business email</option>
        <option value="basic" data-i18n="email_basic">Basic email (Gmail/Yahoo)</option>
        <option value="google" data-i18n="email_google">Google Workspace</option>
        <option value="basic365" data-i18n="email_basic365">Microsoft 365 Basic</option>
        <option value="full365" data-i18n="email_full365">Microsoft 365 Business Premium</option>
      </select>
      <select class="form-select" id="backupStatus" style="margin-bottom:8px;">
        <option value="none" data-i18n="backup_none">No backup</option>
        <option value="usb" data-i18n="backup_usb">USB/Hard drive</option>
        <option value="cloud" data-i18n="backup_cloud">Cloud backup (consumer)</option>
        <option value="business" data-i18n="backup_business">Business-grade backup</option>
      </select>
      <select class="form-select" id="antivirus">
        <option value="none" data-i18n="av_none">No antivirus</option>
        <option value="free" data-i18n="av_free">Free antivirus</option>
        <option value="paid" data-i18n="av_paid">Paid antivirus</option>
        <option value="endpoint" data-i18n="av_endpoint">Enterprise endpoint protection</option>
      </select>
    </div>
    
    <div class="form-group">
      <label class="form-label" data-i18n="budget">Budget Range</label>
      <div class="budget-options">
        <div class="budget-btn active" data-budget="tight" onclick="setBudget('tight')" data-i18n="budget_tight">Tight</div>
        <div class="budget-btn" data-budget="moderate" onclick="setBudget('moderate')" data-i18n="budget_moderate">Moderate</div>
        <div class="budget-btn" data-budget="flexible" onclick="setBudget('flexible')" data-i18n="budget_flexible">Flexible</div>
      </div>
    </div>
    
    <div class="form-group">
      <label class="form-label" data-i18n="addons">Add-ons</label>
      <div class="addon-group">
        <label class="addon-item"><input type="checkbox" id="addon_voip"> <span data-i18n="addon_voip">3CX VoIP Phone System</span></label>
        <label class="addon-item"><input type="checkbox" id="addon_lopdgd"> <span data-i18n="addon_lopdgd">LOPDGDD Compliance Audit</span></label>
        <label class="addon-item"><input type="checkbox" id="addon_nis2"> <span data-i18n="addon_nis2">NIS2 Baseline Assessment</span></label>
        <label class="addon-item"><input type="checkbox" id="addon_extra_ws"> <span data-i18n="addon_extra_ws">Additional Workstation</span></label>
      </div>
    </div>
    
    <button class="btn-generate" id="generateBtn" onclick="generateProposal()" data-i18n="generate">Generate Proposal</button>
  </div>
  
  <!-- Preview Area -->
  <div class="preview" id="preview">
    <div class="preview-empty">
      <div class="preview-empty-icon">&#128203;</div>
      <h3 data-i18n="empty_title">Proposal Preview</h3>
      <p data-i18n="empty_desc">Fill in the client details and click Generate to create a proposal.</p>
    </div>
  </div>
</div>

<script>
// ============ I18N ============
const i18n = {
  en: {
    form_title: "Proposal Configuration",
    company_name: "Company Name",
    website: "Website",
    contact_name: "Contact Name",
    industry: "Industry",
    location: "Location",
    devices: "Devices",
    workstations: "Workstations",
    laptops: "Laptops",
    servers: "Existing Servers",
    current_it: "Current IT State",
    email_none: "No business email",
    email_basic: "Basic email (Gmail/Yahoo)",
    email_google: "Google Workspace",
    email_basic365: "Microsoft 365 Basic",
    email_full365: "Microsoft 365 Business Premium",
    backup_none: "No backup",
    backup_usb: "USB/Hard drive",
    backup_cloud: "Cloud backup (consumer)",
    backup_business: "Business-grade backup",
    av_none: "No antivirus",
    av_free: "Free antivirus",
    av_paid: "Paid antivirus",
    av_endpoint: "Enterprise endpoint protection",
    budget: "Budget Range",
    budget_tight: "Tight",
    budget_moderate: "Moderate",
    budget_flexible: "Flexible",
    addons: "Add-ons",
    addon_voip: "3CX VoIP Phone System",
    addon_lopdgd: "LOPDGDD Compliance Audit",
    addon_nis2: "NIS2 Baseline Assessment",
    addon_extra_ws: "Additional Workstation",
    generate: "Generate Proposal",
    empty_title: "Proposal Preview",
    empty_desc: "Fill in the client details and click Generate to create a proposal.",
    // Proposal text
    ind_legal: "Legal", ind_healthcare: "Healthcare", ind_finance: "Finance",
    ind_retail: "Retail", ind_manufacturing: "Manufacturing", ind_other: "Other",
    loc_spain: "Spain", loc_eu: "European Union", loc_other_other: "Other",
    valid_30: "Valid for 30 Days",
    page_exec_summary: "Executive Summary",
    page_risk: "Risk Assessment",
    page_tiers: "Service Packages",
    page_comparison: "Feature Comparison",
    page_roi: "Return on Investment",
    page_addons: "Optional Add-ons",
    page_next: "Next Steps",
    recommended: "RECOMMENDED",
    recommended_es: "RECOMENDADO",
    per_month: "/month",
    one_time: "One-time:",
    setup_fee: "Setup fee",
    // Exec summary
    exec_intro: "This proposal presents a comprehensive managed IT services plan for {company}, operating in the {industry} industry. Based on our assessment of your current IT infrastructure — {workstations} workstations, {laptops} laptops, and {servers} server(s) — we have designed a layered security and management solution that addresses the specific regulatory and operational requirements of your sector.",
    exec_recommendation: "Recommended Package:",
    exec_recommendation_tier: "{tier} — a robust solution with advanced threat protection, 24/7 monitoring, and regulatory compliance support.",
    // Risk
    risk_title: "Critical Risk Assessment",
    risk_intro: "Without enterprise-grade IT management, {company} faces significant exposure:",
    risk_legal_1: "Client-attorney privilege violations from unencrypted email (LOPDGD fines up to €600,000)",
    risk_legal_2: "Unauthorized access to case files with no conditional access policies",
    risk_legal_3: "Non-compliance with Spain's LOPDGD regarding personal data handling",
    risk_legal_4: "Inability to demonstrate due diligence in data protection audits",
    risk_healthcare_1: "Patient data breaches violating EU GDPR (fines up to €20M or 4% of revenue)",
    risk_healthcare_2: "HIPAA-equivalent compliance failures for medical records",
    risk_healthcare_3: "Critical system downtime affecting patient care delivery",
    risk_healthcare_4: "Ransomware attacks targeting healthcare infrastructure (highest-hit sector)",
    risk_finance_1: "Regulatory non-compliance (Bank of Spain, CNMV, EBA supervisory requirements)",
    risk_finance_2: "Financial data breaches exposing client portfolio information",
    risk_finance_3: "Transaction fraud from compromised email systems (phishing/CEO fraud)",
    risk_finance_4: "Audit failures from inadequate access controls and change management",
    risk_retail_1: "PCI DSS compliance failures exposing customer payment data",
    risk_retail_2: "POS system compromises leading to data theft at scale",
    risk_retail_3: "Supply chain disruption from ransomware across retail operations",
    risk_retail_4: "Inventory and CRM system vulnerabilities from unpatched systems",
    risk_manufacturing_1: "IP theft targeting proprietary designs and manufacturing processes",
    risk_manufacturing_2: "Operational technology (OT) disruption from IT-borne threats",
    risk_manufacturing_3: "Production line shutdowns costing €50,000+/day on average",
    risk_manufacturing_4: "Non-compliance with NIS2 directive for essential service operators",
    risk_other_1: "Data breaches exposing sensitive business and customer information",
    risk_other_2: "Ransomware attacks (60% of small businesses close within 6 months of attack)",
    risk_other_3: "Operational downtime from inadequate backup and recovery systems",
    risk_other_4: "Non-compliance with evolving EU cybersecurity regulations (NIS2)",
    // Tier names
    tier1_name: "Essential",
    tier2_name: "Professional",
    tier3_name: "Enterprise",
    // Tier descriptions
    tier1_desc: "Security foundation & cloud email",
    tier2_desc: "Advanced network protection & monitoring",
    tier3_desc: "Full infrastructure, EDR & compliance",
    // Tier features - UNIQUE per tier
    // Tier 1 features
    t1_f1: "Microsoft 365 Business Premium — business email with custom domain",
    t1_f2: "Multi-Factor Authentication (MFA) — all users",
    t1_f3: "Conditional Access policies — block unauthorized sign-ins",
    t1_f4: "Azure AD P1 — identity & access management",
    t1_f5: "OneDrive for Business — 1TB cloud storage per user",
    t1_f6: "Microsoft Defender for Office — advanced email security",
    t1_f7: "MSP360 cloud backup — all workstations & servers",
    t1_f8: "Backblaze B2 encrypted offsite storage",
    t1_f9: "Dropsuite email backup — point-in-time recovery",
    t1_f10: "Data Processing Agreement (DPA) template",
    t1_f11: "Cyber liability insurance partner referral (€2M coverage)",
    t1_f12: "Client portal — ticket submission & tracking",
    t1_f13: "Monthly backup verification report",
    t1_f14: "Remote helpdesk support (business hours)",
    t1_f15: "3 hours engineer onboarding & setup",
    // Tier 2 additional features
    t2_f1: "FortiGate 60F next-gen firewall — AI-powered threat intelligence",
    t2_f2: "Intrusion Prevention System (IPS) — real-time blocking",
    t2_f3: "Web & DNS filtering — block malicious sites & categories",
    t2_f4: "Email antispam gateway — FortiGuard UTP subscription",
    t2_f5: "VLAN segmentation — isolate critical systems & guest access",
    t2_f6: "Guest Wi-Fi network with captive portal",
    t2_f7: "Site-to-site & remote access VPN",
    t2_f8: "SolarWinds 24/7 RMM — real-time device monitoring & alerting",
    t2_f9: "Automated Windows patch management — critical & security updates",
    t2_f10: "MSP Manager client portal — advanced self-service dashboard",
    t2_f11: "IT Glue self-service knowledge base — How-To guides & FAQs",
    t2_f12: "Continual Improvement Register — tracked IT roadmap",
    t2_f13: "Quarterly Business Reviews (QBR) — strategic IT planning session",
    // Tier 3 additional features
    t3_f1: "Dell T150 server — RAID-1, TrueNAS centralized file storage",
    t3_f2: "Per-user file access permissions & audit logging",
    t3_f3: "Datto SIRIS 5 (2TB SSD) — enterprise backup & disaster recovery",
    t3_f4: "Screenshot backup verification — automatic recovery confirmation",
    t3_f5: "Ransomware detection — automated alerts & instant recovery",
    t3_f6: "Instant virtualization in Datto cloud — <1min RTO",
    t3_f7: "APC Smart-UPS 1500VA — 30-minute runtime, graceful auto-shutdown",
    t3_f8: "SentinelOne Complete — AI-powered endpoint detection & response",
    t3_f9: "Zero-day threat detection — behavioral AI engine",
    t3_f10: "Ransomware kill chain interrupted in <1 second",
    t3_f11: "Auto-remediation — self-healing endpoints, no human intervention",
    t3_f12: "USB device control — block unauthorized peripherals",
    t3_f13: "Forensic storyline — attack timeline reconstruction",
    t3_f14: "Annual compliance review — DPO advisory & LOPDGD gap analysis",
    t3_f15: "NIS2 baseline controls checklist & remediation plan",
    // Tier does NOT include
    tier1_not_incl: "Does not include: Server, firewall, 24/7 monitoring, DR, compliance audit",
    tier2_not_incl: "Does not include: Centralized server, disaster recovery, SentinelOne EDR, compliance audit",
    tier3_not_incl: "Everything included — full-scope enterprise solution",
    // Comparison
    comp_feature: "Feature",
    comp_tier1: "Essential",
    comp_t2: "Professional",
    comp_t3: "Enterprise",
    // ROI
    roi_without: "Without Protection",
    roi_with: "With Protection",
    roi_avg_breach: "Avg. data breach cost:",
    roi_downtime: "Monthly downtime cost:",
    roi_compliance: "Regulatory non-compliance risk:",
    roi_recovery: "Recovery time from incident:",
    roi_breach_legal: "€150,000 - €600,000",
    roi_breach_healthcare: "€500,000 - €20M",
    roi_breach_finance: "€300,000 - €5M+",
    roi_breach_retail: "€100,000 - €2M",
    roi_breach_manufacturing: "€200,000 - €5M",
    roi_breach_other: "€50,000 - €500,000",
    roi_downtime_val: "€5,000 - €50,000",
    roi_compliance_high: "HIGH — fines, sanctions, litigation",
    roi_compliance_none: "NONE — fully compliant",
    roi_recovery_long: "Days to weeks (if recoverable)",
    roi_recovery_short: "Minutes to hours",
    roi_annual_spend: "Annual protection investment:",
    roi_risk_reduction: "Risk reduction:",
    roi_risk_reduction_val: "94% (based on industry data)",
    // Next steps
    next_title: "Ready to Secure Your Business?",
    next_desc: "This proposal is valid for 30 days. Contact us to schedule your onboarding kickoff.",
    next_cta: "Download PDF",
    next_step1: "Schedule discovery call",
    next_step2: "Sign service agreement",
    next_step3: "Onboarding kickoff (Week 1)",
    next_step4: "Migration & deployment (Weeks 2-3)",
    next_step5: "Go-live & monitoring active (Week 4)",
    // Internal
    internal_cost_breakdown: "Cost Breakdown (Internal)",
    internal_item: "Item",
    internal_cost: "Cost",
    internal_sell: "Sell Price",
    internal_margin: "Margin",
    internal_monthly_summary: "Monthly Summary",
    internal_one_time_summary: "One-Time Summary",
    internal_total_project: "Total Project Revenue (Year 1):",
    internal_blended_margin: "Blended Margin:",
    internal_engineer_workflow: "Engineer Workflow",
    internal_objection_handling: "Objection Handling",
    obj_q1: "\"This is too expensive.\"",
    obj_a1: "Frame the cost of inaction: a single ransomware incident averages €200K+ for SMBs. Our Enterprise tier costs {annual_cost}/year — that's less than one day of downtime. Plus, 60% of small businesses that suffer a major breach close within 6 months.",
    obj_q2: "\"We already have an IT person.\"",
    obj_a2: "Great — they handle day-to-day issues. Our 24/7 monitoring catches threats at 3 AM when your IT person is asleep. We handle patching, backups, firewall management, and compliance — freeing your IT person to focus on strategic projects.",
    obj_q3: "\"We've never been hacked.\"",
    obj_a3: "The average time to detect a breach is 204 days. Attackers are already inside most networks — they just haven't acted yet. Cyber insurance providers now require MFA, endpoint protection, and backups as minimum requirements.",
    obj_q4: "\"We'll think about it.\"",
    obj_a4: "Totally understand. Meanwhile, every day without proper protection, your business is exposed. Can we schedule a 15-minute follow-up next week? I'll prepare a specific risk analysis for your industry.",
    obj_q5: "\"Our current setup works fine.\"",
    obj_a5: "It's working until it doesn't. The question isn't whether you'll have an incident — it's when, and whether you'll recover. Our backup solution guarantees recovery within minutes, not days.",
    step1: "Discovery call — assess current IT state, identify gaps",
    step2: "Proposal delivery & customization — align with budget & priorities",
    step3: "Contract execution — sign MSA + SOW, collect deposit",
    step4: "Onboarding Phase 1 — deploy M365, configure MFA & Conditional Access",
    step5: "Onboarding Phase 2 — install firewall, configure VLANs & VPN",
    step6: "Onboarding Phase 3 — deploy RMM, backup agents, patch management",
    step7: "Migration — email migration, server setup, file consolidation",
    step8: "Go-live — monitoring active, client portal access, training",
    step9: "First QBR — review metrics, present improvement register",
    addon_voip_title: "3CX VoIP",
    addon_voip_desc: "Professional phone system with mobile apps, call queues & CRM integration",
    addon_lopdgd_title: "LOPDGDD Audit",
    addon_lopdgd_desc: "Full compliance review by DPO-certified consultant — gap analysis & remediation plan",
    addon_nis2_title: "NIS2 Assessment",
    addon_nis2_desc: "Baseline assessment against EU NIS2 directive requirements with prioritized remediation plan",
    addon_extra_ws_title: "Additional Workstation",
    addon_extra_ws_desc: "Out-of-scope workstation deployment — standard configuration included",
    scrape_loading: "Checking...",
    scrape_success: "OK",
    scrape_error: "N/A",
  },
  es: {
    form_title: "Configuración de Propuesta",
    company_name: "Nombre de Empresa",
    website: "Sitio Web",
    contact_name: "Nombre de Contacto",
    industry: "Industria",
    location: "Ubicación",
    devices: "Dispositivos",
    workstations: "Equipos de Escritorio",
    laptops: "Portátiles",
    servers: "Servidores Existentes",
    current_it: "Estado Actual de TI",
    email_none: "Sin email empresarial",
    email_basic: "Email básico (Gmail/Yahoo)",
    email_google: "Google Workspace",
    email_basic365: "Microsoft 365 Básico",
    email_full365: "Microsoft 365 Business Premium",
    backup_none: "Sin copias de seguridad",
    backup_usb: "USB/Disco duro",
    backup_cloud: "Backup en la nube (consumidor)",
    backup_business: "Backup empresarial",
    av_none: "Sin antivirus",
    av_free: "Antivirus gratuito",
    av_paid: "Antivirus de pago",
    av_endpoint: "Protección empresarial de endpoints",
    budget: "Rango de Presupuesto",
    budget_tight: "Ajustado",
    budget_moderate: "Moderado",
    budget_flexible: "Flexible",
    addons: "Complementos",
    addon_voip: "Sistema Telefónico 3CX VoIP",
    addon_lopdgd: "Auditoría de Cumplimiento LOPDGD",
    addon_nis2: "Evaluación Baseline NIS2",
    addon_extra_ws: "Equipo de Escritorio Adicional",
    generate: "Generar Propuesta",
    empty_title: "Vista Previa de Propuesta",
    empty_desc: "Complete los datos del cliente y haga clic en Generar para crear una propuesta.",
    ind_legal: "Legal", ind_healthcare: "Sanidad", ind_finance: "Finanzas",
    ind_retail: "Retail", ind_manufacturing: "Manufactura", ind_other: "Otro",
    loc_spain: "España", loc_eu: "Unión Europea", loc_other_other: "Otro",
    valid_30: "Válido por 30 Días",
    page_exec_summary: "Resumen Ejecutivo",
    page_risk: "Evaluación de Riesgos",
    page_tiers: "Paquetes de Servicio",
    page_comparison: "Comparativa de Funcionalidades",
    page_roi: "Retorno de Inversión",
    page_addons: "Complementos Opcionales",
    page_next: "Próximos Pasos",
    recommended: "RECOMENDADO",
    recommended_es: "RECOMENDADO",
    per_month: "/mes",
    one_time: "Pago único:",
    setup_fee: "Cuota de instalación",
    exec_intro: "Esta propuesta presenta un plan integral de servicios gestionados de TI para {company}, que opera en el sector {industry}. Basándonos en nuestra evaluación de su infraestructura actual de TI — {workstations} equipos de escritorio, {laptops} portátiles y {servers} servidor(es) — hemos diseñado una solución de seguridad y gestión por capas que aborda los requisitos normativos y operativos específicos de su sector.",
    exec_recommendation: "Paquete Recomendado:",
    exec_recommendation_tier: "{tier} — una solución robusta con protección avanzada contra amenazas, monitorización 24/7 y soporte de cumplimiento normativo.",
    risk_title: "Evaluación Crítica de Riesgos",
    risk_intro: " Sin una gestión de TI de nivel empresarial, {company} enfrenta una exposición significativa:",
    risk_legal_1: "Violaciones del secreto profesional por email no cifrado (multas LOPDGD de hasta €600.000)",
    risk_legal_2: "Acceso no autorizado a expedientes sin políticas de acceso condicional",
    risk_legal_3: "Incumplimiento de la LOPDGD de España sobre tratamiento de datos personales",
    risk_legal_4: "Imposibilidad de demostrar diligencia debida en auditorías de protección de datos",
    risk_healthcare_1: "Filtraciones de datos de pacientes violando el RGPD de la UE (multas de hasta €20M)",
    risk_healthcare_2: "Fallos de cumplimiento equivalentes a HIPAA para historiales médicos",
    risk_healthcare_3: "Tiempo de inactividad crítico afectando la atención al paciente",
    risk_healthcare_4: "Ataques de ransomware dirigidos a infraestructura sanitaria (sector más afectado)",
    risk_finance_1: "Incumplimiento regulatorio (Banco de España, CNMV, requisitos supervisorios de la EBA)",
    risk_finance_2: "Filtraciones de datos financieros que exponen información de carteras de clientes",
    risk_finance_3: "Fraude en transacciones por sistemas de email comprometidos (phishing/fraude CEO)",
    risk_finance_4: "Fallos de auditoría por controles de acceso y gestión de cambios inadecuados",
    risk_retail_1: "Fallos de cumplimiento PCI DSS que exponen datos de pago de clientes",
    risk_retail_2: "Compromisos en sistemas de punto de venta (POS) que conducen a robo de datos masivo",
    risk_retail_3: "Interrupción de la cadena de suministro por ransomware en operaciones de retail",
    risk_retail_4: "Vulnerabilidades en sistemas de inventario y CRM por sistemas sin actualizar",
    risk_manufacturing_1: "Robo de propiedad intelectual — diseños y procesos de manufactura",
    risk_manufacturing_2: "Disrupción de tecnología operativa (OT) por amenazas de TI",
    risk_manufacturing_3: "Paradas de línea de producción con costes de €50.000+/día de media",
    risk_manufacturing_4: "Incumplimiento de la directiva NIS2 para operadores de servicios esenciales",
    risk_other_1: "Filtraciones de datos que exponen información comercial y de clientes",
    risk_other_2: "Ataques de ransomware (el 60% de las pequeñas empresas cierran en 6 meses tras un ataque)",
    risk_other_3: "Tiempo de inactividad operativa por sistemas de backup y recuperación inadecuados",
    risk_other_4: "Incumplimiento de la normativa de ciberseguridad de la UE en evolución (NIS2)",
    tier1_name: "Esencial",
    tier2_name: "Profesional",
    tier3_name: "Empresarial",
    tier1_desc: "Base de seguridad y email en la nube",
    tier2_desc: "Protección de red avanzada y monitorización",
    tier3_desc: "Infraestructura completa, EDR y cumplimiento",
    t1_f1: "Microsoft 365 Business Premium — email empresarial con dominio personalizado",
    t1_f2: "Autenticación Multifactor (MFA) — todos los usuarios",
    t1_f3: "Políticas de Acceso Condicional — bloqueo de accesos no autorizados",
    t1_f4: "Azure AD P1 — gestión de identidad y accesos",
    t1_f5: "OneDrive for Business — 1TB de almacenamiento en la nube por usuario",
    t1_f6: "Microsoft Defender for Office — seguridad avanzada de email",
    t1_f7: "MSP360 backup en la nube — todos los equipos y servidores",
    t1_f8: "Almacenamiento offsite cifrado Backblaze B2",
    t1_f9: "Dropsuite backup de email — recuperación en punto temporal",
    t1_f10: "Plantilla de Acuerdo de Tratamiento de Datos (DPA)",
    t1_f11: "Seguro de responsabilidad cibernética (€2M de cobertura)",
    t1_f12: "Portal de cliente — envío y seguimiento de tickets",
    t1_f13: "Informe mensual de verificación de backups",
    t1_f14: "Soporte helpdesk remoto (horario laboral)",
    t1_f15: "3 horas de incorporación y configuración por ingeniero",
    t2_f1: "FortiGate 60F firewall de próxima generación — inteligencia de amenazas con IA",
    t2_f2: "Sistema de Prevención de Intrusiones (IPS) — bloqueo en tiempo real",
    t2_f3: "Filtrado web y DNS — bloqueo de sitios y categorías maliciosas",
    t2_f4: "Pasarela antispam de email — suscripción FortiGuard UTP",
    t2_f5: "Segmentación VLAN — aislar sistemas críticos y acceso de invitados",
    t2_f6: "Red Wi-Fi de invitados con portal cautivo",
    t2_f7: "VPN sitio-a-sitio y acceso remoto",
    t2_f8: "SolarWinds RMM 24/7 — monitorización y alertas en tiempo real",
    t2_f9: "Gestión automatizada de parches de Windows",
    t2_f10: "Portal de cliente MSP Manager — panel de autoservicio avanzado",
    t2_f11: "Base de conocimiento de autoservicio IT Glue",
    t2_f12: "Registro de Mejora Continua — hoja de ruta de TI",
    t2_f13: "Revisiones Trimestrales de Negocio (QBR)",
    t3_f1: "Servidor Dell T150 — RAID-1, almacenamiento centralizado TrueNAS",
    t3_f2: "Permisos de acceso por usuario y registro de auditoría",
    t3_f3: "Datto SIRIS 5 (2TB SSD) — backup empresarial y recuperación ante desastres",
    t3_f4: "Verificación de backups por capturas de pantalla — confirmación automática",
    t3_f5: "Detección de ransomware — alertas automáticas y recuperación instantánea",
    t3_f6: "Virtualización instantánea en nube Datto — <1min RTO",
    t3_f7: "APC Smart-UPS 1500VA — 30 minutos de autonomía, apagado automático controlado",
    t3_f8: "SentinelOne Complete — detección y respuesta de endpoints con IA",
    t3_f9: "Detección de amenazas zero-day — motor de IA conductual",
    t3_f10: "Interrupción de cadena de ransomware en <1 segundo",
    t3_f11: "Autorremediación — endpoints de autocuración",
    t3_f12: "Control de dispositivos USB — bloqueo de periféricos no autorizados",
    t3_f13: "Cronología forense — reconstrucción de línea temporal del ataque",
    t3_f14: "Revisión anual de cumplimiento — asesor DPO y análisis de brechas LOPDGD",
    t3_f15: "Checklist de controles baseline NIS2 y plan de remediación",
    tier1_not_incl: "No incluye: Servidor, firewall, monitorización 24/7, DR, auditoría de cumplimiento",
    tier2_not_incl: "No incluye: Servidor centralizado, recuperación ante desastres, SentinelOne EDR, auditoría de cumplimiento",
    tier3_not_incl: "Todo incluido — solución empresarial completa",
    comp_feature: "Funcionalidad",
    comp_tier1: "Esencial",
    comp_t2: "Profesional",
    comp_t3: "Empresarial",
    roi_without: "Sin Protección",
    roi_with: "Con Protección",
    roi_avg_breach: "Coste promedio de filtración:",
    roi_downtime: "Coste mensual de inactividad:",
    roi_compliance: "Riesgo de incumplimiento normativo:",
    roi_recovery: "Tiempo de recuperación ante incidente:",
    roi_breach_legal: "€150.000 - €600.000",
    roi_breach_healthcare: "€500.000 - €20M",
    roi_breach_finance: "€300.000 - €5M+",
    roi_breach_retail: "€100.000 - €2M",
    roi_breach_manufacturing: "€200.000 - €5M",
    roi_breach_other: "€50.000 - €500.000",
    roi_downtime_val: "€5.000 - €50.000",
    roi_compliance_high: "ALTO — multas, sanciones, litigios",
    roi_compliance_none: "NINGUNO — totalmente cumpliente",
    roi_recovery_long: "Días a semanas (si es recuperable)",
    roi_recovery_short: "Minutos a horas",
    roi_annual_spend: "Inversión anual en protección:",
    roi_risk_reduction: "Reducción de riesgo:",
    roi_risk_reduction_val: "94% (según datos del sector)",
    next_title: "¿Listo para Proteger Su Negocio?",
    next_desc: "Esta propuesta es válida por 30 días. Contáctenos para programar la sesión de incorporación.",
    next_cta: "Descargar PDF",
    next_step1: "Programar llamada de descubrimiento",
    next_step2: "Firmar acuerdo de servicio",
    next_step3: "Inicio de incorporación (Semana 1)",
    next_step4: "Migración y despliegue (Semanas 2-3)",
    next_step5: "Puesta en marcha y monitorización activa (Semana 4)",
    internal_cost_breakdown: "Desglose de Costes (Interno)",
    internal_item: "Elemento",
    internal_cost: "Coste",
    internal_sell: "Precio Venta",
    internal_margin: "Margen",
    internal_monthly_summary: "Resumen Mensual",
    internal_one_time_summary: "Resumen Pago Único",
    internal_total_project: "Ingresos Totales del Proyecto (Año 1):",
    internal_blended_margin: "Margen Combinado:",
    internal_engineer_workflow: "Flujo de Trabajo del Ingeniero",
    internal_objection_handling: "Manejo de Objeciones",
    obj_q1: "\"Esto es demasiado caro.\"",
    obj_a1: "Enfocar el coste de la inacción: un único incidente de ransomware promedia más de €200K para PYMES. Nuestro nivel Empresarial cuesta {annual_cost}/año — eso es menos que un día de inactividad. Además, el 60% de las pequeñas empresas que sufren una brecha grave cierran en 6 meses.",
    obj_q2: "\"Ya tenemos una persona de TI.\"",
    obj_a3: "Genial — ellos manejan el día a día. Nuestra monitorización 24/7 detecta amenazas a las 3 AM cuando su persona de TI está durmiendo. Nosotros manejamos parches, backups, firewall y cumplimiento — liberando a su persona de TI para proyectos estratégicos.",
    obj_q3: "\"Nunca nos han hackeado.\"",
    obj_a3: "El tiempo promedio para detectar una brecha es de 204 días. Los atacantes ya están dentro de la mayoría de las redes — simplemente aún no han actuado. Los proveedores de seguros cibernéticos ahora requieren MFA, protección de endpoints y backups como requisitos mínimos.",
    obj_q4: "\"Lo pensaremos.\"",
    obj_a4: "Totalmente entendido. Mientras tanto, cada día sin protección adecuada, su negocio está expuesto. ¿Podemos programar un seguimiento de 15 minutos la próxima semana? Prepararé un análisis de riesgos específico para su sector.",
    obj_q5: "\"Nuestra configuración actual funciona bien.\"",
    obj_a5: "Funciona hasta que deja de funcionar. La pregunta es si tendrá un incidente — sino cuándo, y si se recuperará. Nuestra solución de backup garantiza recuperación en minutos, no días.",
    step1: "Llamada de descubrimiento — evaluar estado de TI actual, identificar brechas",
    step2: "Entrega y personalización de propuesta — alinear con presupuesto y prioridades",
    step3: "Ejecución del contrato — firmar MSA + SOW, recoger depósito",
    step4: "Incorporación Fase 1 — desplegar M365, configurar MFA y Acceso Condicional",
    step5: "Incorporación Fase 2 — instalar firewall, configurar VLANs y VPN",
    step6: "Incorporación Fase 3 — desplegar RMM, agentes de backup, gestión de parches",
    step7: "Migración — migración de email, configuración de servidor, consolidación de archivos",
    step8: "Puesta en marcha — monitorización activa, acceso al portal, formación",
    step9: "Primer QBR — revisar métricas, presentar registro de mejora",
    addon_voip_title: "3CX VoIP",
    addon_voip_desc: "Sistema telefónico profesional con apps móviles, colas de llamadas e integración CRM",
    addon_lopdgd_title: "Auditoría LOPDGD",
    addon_lopdgd_desc: "Revisión completa de cumplimiento por consultor certificado DPO — análisis de brechas y plan de remediación",
    addon_nis2_title: "Evaluación NIS2",
    addon_nis2_desc: "Evaluación baseline contra requisitos de la directiva NIS2 de la UE con plan de remediación priorizado",
    addon_extra_ws_title: "Equipo Adicional",
    addon_extra_ws_desc: "Despliegue de equipo fuera del alcance — configuración estándar incluida",
    scrape_loading: "Verificando...",
    scrape_success: "OK",
    scrape_error: "N/A",
  }
};

// Fix Spanish obj_q2 key
i18n.es.obj_q2 = "\"Ya tenemos una persona de TI.\"";
i18n.es.obj_a2 = "Genial — ellos manejan el día a día. Nuestra monitorización 24/7 detecta amenazas a las 3 AM cuando su persona de TI está durmiendo. Nosotros manejamos parches, backups, firewall y cumplimiento — liberando a su persona de TI para proyectos estratégicos.";
i18n.es.obj_q3 = "\"Nunca nos han hackeado.\"";
i18n.es.obj_a3 = "El tiempo promedio para detectar una brecha es de 204 días. Los atacantes ya están dentro de la mayoría de las redes — simplemente aún no han actuado. Los proveedores de seguros cibernéticos ahora requieren MFA, protección de endpoints y backups como requisitos mínimos.";
i18n.es.obj_q4 = "\"Lo pensaremos.\"";
i18n.es.obj_a4 = "Totalmente entendido. Mientras tanto, cada día sin protección adecuada, su negocio está expuesto. ¿Podemos programar un seguimiento de 15 minutos la próxima semana? Prepararé un análisis de riesgos específico para su sector.";
i18n.es.obj_q5 = "\"Nuestra configuración actual funciona bien.\"";
i18n.es.obj_a5 = "Funciona hasta que deja de funcionar. La pregunta no es si tendrá un incidente — sino cuándo, y si se recuperará. Nuestra solución de backup garantiza recuperación en minutos, no días.";

var currentLang = 'en';
var currentView = 'client';
var currentBudget = 'tight';

function t(key) {
  return i18n[currentLang][key] || i18n.en[key] || key;
}

function setLang(lang) {
  currentLang = lang;
  document.querySelectorAll('.lang-btn').forEach(function(b){ b.classList.toggle('active', b.dataset.lang === lang); });
  document.querySelectorAll('[data-i18n]').forEach(function(el) {
    var key = el.dataset.i18n;
    if (i18n[lang][key]) el.textContent = i18n[lang][key];
  });
  var preview = document.getElementById('preview');
  if (preview.dataset.generated === 'true') generateProposal();
}

function setView(view) {
  currentView = view;
  document.querySelectorAll('.view-btn').forEach(function(b){ b.classList.toggle('active', b.dataset.view === view); });
  var preview = document.getElementById('preview');
  if (preview.dataset.generated === 'true') generateProposal();
}

function setBudget(b) {
  currentBudget = b;
  document.querySelectorAll('.budget-btn').forEach(function(btn){
    btn.classList.toggle('active', btn.dataset.budget === b);
  });
}

function adjustNum(id, delta) {
  var el = document.getElementById(id);
  var val = parseInt(el.value) || 0;
  val = Math.max(0, Math.min(500, val + delta));
  el.value = val;
}

// ============ PRICING ENGINE ============
var PRICING = {
  hardware: {
    dell_t150:    { cost: 800,  sell: 1200 },
    fortigate_60f:{ cost: 735,  sell: 1290 },
    datto_siris:  { cost: 1500, sell: 2400 },
    apc_ups:      { cost: 200,  sell: 350  },
  },
  software: {
    m365_bp:       { cost: 18.70, sell: 22.50, unit: 'user' },
    dropsuite:     { cost: 3.00,  sell: 4.50,  unit: 'user' },
    msp360:        { cost: 5.00,  sell: 8.33,  unit: 'device' },
    backblaze_b2:  { cost: 10,    sell: 10,    unit: 'fixed' },
    sentinelone:   { cost: 2.50,  sell: 5.00,  unit: 'endpoint' },
    solarwinds:    { cost: 20,    sell: 20,    unit: 'fixed' },
    voip_3cx:      { cost: 12,    sell: 20,    unit: 'user' },
  },
  labor: {
    tier1_hours: 3, tier1_monthly: 60,
    tier2_hours: 5, tier2_monthly: 100,
    tier3_hours: 10, tier3_monthly: 200,
    blended_rate: 20,
  },
  onetime: {
    tier1_setup: 299,
    addon_voip: 500,
    addon_extra_ws: 199,
  }
};

function calcPricing(inputs) {
  var users = inputs.workstations + inputs.laptops;
  var devices = inputs.workstations + inputs.laptops + Math.max(1, inputs.servers);
  var endpoints = users + Math.max(1, inputs.servers);
  
  // Base user/device software costs
  var m365_monthly_cost = users * PRICING.software.m365_bp.cost;
  var m365_monthly_sell = users * PRICING.software.m365_bp.sell;
  var dropsuite_monthly_cost = users * PRICING.software.dropsuite.cost;
  var dropsuite_monthly_sell = users * PRICING.software.dropsuite.sell;
  var msp360_monthly_cost = devices * PRICING.software.msp360.cost;
  var msp360_monthly_sell = devices * PRICING.software.msp360.sell;
  var b2_monthly = 10; // fixed
  
  // TIER 1
  var t1_monthly_cost = m365_monthly_cost + msp360_monthly_cost + b2_monthly + dropsuite_monthly_cost + PRICING.labor.tier1_monthly;
  var t1_monthly_sell = m365_monthly_sell + msp360_monthly_sell + b2_monthly + dropsuite_monthly_sell + PRICING.labor.tier1_monthly;
  var t1_onetime_cost = PRICING.onetime.tier1_setup;
  var t1_onetime_sell = PRICING.onetime.tier1_setup;
  
  // TIER 2 (cumulative)
  var t2_extra_monthly_cost = PRICING.software.solarwinds.cost + (PRICING.labor.tier2_monthly - PRICING.labor.tier1_monthly);
  var t2_extra_monthly_sell = PRICING.software.solarwinds.sell + (PRICING.labor.tier2_monthly - PRICING.labor.tier1_monthly);
  var t2_monthly_cost = t1_monthly_cost + t2_extra_monthly_cost;
  var t2_monthly_sell = t1_monthly_sell + t2_extra_monthly_sell;
  var t2_onetime_cost = t1_onetime_cost + PRICING.hardware.fortigate_60f.cost;
  var t2_onetime_sell = t1_onetime_sell + PRICING.hardware.fortigate_60f.sell;
  
  // TIER 3 (cumulative)
  var s1_cost = endpoints * PRICING.software.sentinelone.cost;
  var s1_sell = endpoints * PRICING.software.sentinelone.sell;
  var t3_extra_labor = PRICING.labor.tier3_monthly - PRICING.labor.tier2_monthly;
  var t3_monthly_cost = t2_monthly_cost + s1_cost + t3_extra_labor;
  var t3_monthly_sell = t2_monthly_sell + s1_sell + t3_extra_labor;
  var t3_onetime_cost = t2_onetime_cost + PRICING.hardware.dell_t150.cost + PRICING.hardware.datto_siris.cost + PRICING.hardware.apc_ups.cost + 800;
  var t3_onetime_sell = t2_onetime_sell + PRICING.hardware.dell_t150.sell + PRICING.hardware.datto_siris.sell + PRICING.hardware.apc_ups.sell + 800;
  
  // Add-ons
  var voip_monthly_cost = inputs.addons.voip ? users * PRICING.software.voip_3cx.cost : 0;
  var voip_monthly_sell = inputs.addons.voip ? users * PRICING.software.voip_3cx.sell : 0;
  var voip_onetime = inputs.addons.voip ? PRICING.onetime.addon_voip : 0;
  var extra_ws_monthly = input