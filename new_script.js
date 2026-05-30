// SMGTEC Proposal Generator v2.0
var P={m365_bp:{c:18.70,s:22.50},dropsuite:{c:3.00,s:4.50},msp360:{c:5.00,s:8.33},b2:10,fortigate_60f:{c:735,s:1290},fortigate_utp:{c:503},solarwinds:20,sentinelone:{c:2.50,s:5.00},dell_t150:{c:800,s:1200},datto_siris5:{c:1500,s:2400},apc_ups:{c:200,s:350},voip_3cx:{c:12,s:20},labor_h:20,setup1:120,setup2:150,setup3:800};
var IND={legal:{en:'Legal',es:'Legal',risks:['Client confidentiality breach — up to €10M LOPDGD fines','Email contains case evidence — must be backed up','Unauthorized access — personal liability']},healthcare:{en:'Healthcare',es:'Sanidad',risks:['Patient data — strict confidentiality','Medical records must be retained 5+ years','Unauthorized access — criminal liability']},finance:{en:'Finance',es:'Finanzas',risks:['Financial data — NIS2 compliance required','Transaction audit trails mandatory','Enhanced data protection for assets']},retail:{en:'Retail',es:'Retail',risks:['Customer payment data — PCI-DSS requirements','Personal data processing — consent management','E-commerce platform — uptime critical']},other:{en:'Professional Services',es:'Servicios Profesionales',risks:['Client data protection — LOPDGD compliance','Professional liability — data breach','Reputational damage — client trust']}};
var L='en';
var I={en:{sec_company:'Company Information',f_company:'Company Name',f_website:'Website (optional)',f_contact:'Contact Name',f_industry:'Industry',sec_infra:'IT Infrastructure',f_ws:'Workstations',f_lap:'Laptops',f_srv:'Servers',f_budget:'Budget Range',sec_state:'Current IT State',f_email:'Email',f_backup:'Backup',btn_gen:'Generate Proposal',generating:'Generating...',empty_t:'No proposal yet',empty_d:'Fill in the company details and click Generate.',preparedFor:'Prepared for',validFor:'Valid for 30 days',execSummary:'Executive Summary',riskAssess:'Risk Assessment',oneTime:'One-time',perMonth:'/month',roi:'The Math That Matters',without:'Without Protection',withProtection:'With Protection',comparison:'Comparison',addOns:'Available Add-Ons',nextStep:'Next Step',nextStepTxt:'One decision. Sign. We build.',intTitle:'Internal Briefing',costBreak:'Cost Breakdown',module:'Module',ourCost:'Our Cost',clientPays:'Client Pays',margin:'Margin',total:'Total',profit:'Profit',wfTitle:'Workflow',objTitle:'Objections'}};var I_ES={sec_company:'Información de la Empresa',f_company:'Nombre',f_website:'Sitio Web',f_contact:'Contacto',f_industry:'Industria',sec_infra:'Infraestructura IT',f_ws:'Ordenadores',f_lap:'Portátiles',f_srv:'Servidores',f_budget:'Presupuesto',sec_state:'Estado Actual',f_email:'Email',f_backup:'Backup',btn_gen:'Generar Propuesta',generating:'Generando...',empty_t:'Aún no hay propuesta',empty_d:'Complete los datos y haga clic en Generar.',preparedFor:'Preparado para',validFor:'Válido 30 días',execSummary:'Resumen Ejecutivo',riskAssess:'Evaluación de Riesgos',oneTime:'Pago único',perMonth:'/mes',roi:'Las Cuentas',without:'Sin Protección',withProtection:'Con Protección',comparison:'Comparativa',addOns:'Módulos Adicionales',nextStep:'Siguiente Paso',nextStepTxt:'Una decisión. Firma. Construimos.',intTitle:'Briefing Interno',costBreak:'Desglose de Costes',module:'Módulo',ourCost:'Nuestro Coste',clientPays:'Cliente Paga',margin:'Margen',total:'Total',profit:'Beneficio',wfTitle:'Cronograma',objTitle:'Objeciones'};
function t(k){return(L==='es'&&I_ES[k])||I[k];}
function setLang(l){L=l;document.querySelectorAll('.lang-btn').forEach(function(b,i){b.classList.toggle('active',(i===0&&l==='en')||(i===1&&l==='es'))});updateLabels();}
function setMode(m){
  document.getElementById('mClient').classList.toggle('active',m==='client');
  document.getElementById('mInternal').classList.toggle('active',m==='internal');
  var p=document.getElementById('proposal'),ib=document.getElementById('internalBrief');
  p.style.display=m==='client'?'block':'none';
  ib.style.display=m==='internal'?'block':'none';
  if(m==='client'){ib.innerHTML='';document.getElementById('btnGen').textContent=t('btn_gen');}
}
function updateLabels(){document.querySelectorAll('[data-i18n]').forEach(function(el){var k=el.getAttribute('data-i18n');if(['company','companyName','website','contactName','infrastructure','workstations','laptops','servers','budgetRange','currentState','currentEmail','currentBackup','generate','emptyTitle','emptyDesc'].indexOf(k)>=0)el.innerHTML=t(k);});}
function adj(id,d){var el=document.getElementById(id);el.value=Math.max(0,(parseInt(el.value)||0)+d);}

function calc(){
  var u=(parseInt(document.getElementById('v_ws').value)||0)+(parseInt(document.getElementById('v_lap').value)||0);
  var dev=u+(parseInt(document.getElementById('v_srv').value)||0);
  var eps=dev;
  var b=document.getElementById('f_budget').value;
  var rules=IND[document.getElementById('f_industry').value]||IND.other;

  // TIER 1
  var t1m=(P.m365_bp.s*u)+(P.msp360.s*dev)+P.b2+(P.dropsuite.s*u)+(P.labor_h*3);
  var t1ot=299;
  var t1cm=(P.m365_bp.c*u)+(P.msp360.c*dev)+P.b2+(P.dropsuite.c*u)+(P.labor_h*3);
  var t1ct=P.setup1;

  // TIER 2 (=Tier 1 + additions)
  var fm=P.fortigate_utp.c/12;
  var t2m=t1m+fm+P.solarwinds+(P.labor_h*2);
  var t2ot=t1ot+P.fortigate_60f.s;
  var t2cm=t1cm+fm+P.solarwinds+(P.labor_h*2);
  var t2ct=t1ct+P.fortigate_60f.c;

  // TIER 3 (=Tier 2 + additions)
  var sm=P.sentinelone.s*eps,sc=P.sentinelone.c*eps;
  var t3m=t2m+sm+300;
  var t3ot=t2ot+P.dell_t150.s+P.datto_siris5.s+P.apc_ups.s+1000;
  var t3cm=t2cm+sc+(P.labor_h*3);
  var t3ct=t2ct+P.dell_t150.c+P.datto_siris5.c+P.apc_ups.c+P.setup3;

  [t1m,t2m,t3m,t2ot,t3ot].forEach(function(v,i){[t1m,t2m,t3m,t2ot,t3ot][i]=Math.round(v);});

  function tierData(mo,ot,cm,ct){
    var yr=ot+mo*12,yc=ct+cm*12,p=yr-yc;
    var mg=yr>0?Math.round(p/yr*100):0;
    return{mo:mo,ot:ot,cm:cm,ct:ct,yr:yr,yc:yc,p:p,m:mg};
  }
  return{
    t1:tierData(t1m,t1ot,t1cm,t1ct),
    t2:tierData(t2m,t2ot,t2cm,t2ct),
    t3:tierData(t3m,t3ot,t3cm,t3ct),
    u:u,dev:dev,rules:rules,budget:b
  };
}

function gen(){
  var btn=document.getElementById('btnGen');
  btn.disabled=true;btn.textContent=t('generating');
  setTimeout(function(){
    var d=calc();
    var isES=L==='es';
    var co=document.getElementById('f_company').value||'Client';
    var ct=document.getElementById('f_contact').value||'';
    var rec=d.budget==='flexible'?3:d.budget==='tight'?1:2;
    var cp=document.getElementById('proposal');
    cp.innerHTML='';cp.classList.add('visible');
    document.getElementById('internalBrief').classList.remove('visible');
    document.getElementById('emptySt').style.display='none';

    function page(h){var dv=document.createElement('div');dv.className='pp';dv.innerHTML=h;cp.appendChild(dv);}

    // COVER
    page('<div class="pp-cover"><div class="pp-logo">SMGTEC SL</div>'+
      '<h1 class="pp-title">'+t('execSummary').replace('Executive Summary',L==='en'?'Infrastructure Proposal':'Propuesta')+'</h1>'+
      '<div class="pp-sub">'+t('comparison').replace('Comparison','Data Protection + Security')+'</div>'+
      '<div class="pp-client"><strong>'+t('preparedFor')+':</strong> '+co+' '+(ct?'— '+ct:'')+'</div>'+
      '<div class="pp-valid">'+t('validFor')+' '+new Date().toLocaleDateString(isES?'es-US':'en-US')+'</div></div>');

    // EXECUTIVE SUMMARY
    page('<div class="pp-body"><div class="ps"><h2 class="ps-title">'+t('execSummary')+'</h2>'+
      '<p>'+(isES?co+' es un '+d.rules.es+'. Sin backup ni protección — tres niveles propuestos.':co+' is a '+d.rules.en+' firm. No backup or protection — three tiers proposed.')+'</p></div></div>');

    // RISK
    var rh='<div class="pp-body"><div class="ps"><h2 class="ps-title">'+t('riskAssess')+'</h2>'+
      '<div class="risk-box"><h4>'+(isES?'Riesgos':'Risks')+'</h4><ul class="tier-card-features">';
    d.rules.risks.forEach(function(r){rh+='<li class="included">'+r+'</li>';});
    rh+='</ul></div></div></div>';
    page(rh);

    // TIER CARDS — DISTINCT feature lists
    var f1=[t('execSummary').replace('Executive Summary','M365 BP')+' — email, MFA, Conditional Access, Defender for Business',
             'MSP360 cloud backup — encrypted, off-site, ransomware-proof',
             'Dropsuite email backup — all mailboxes, 1yr retention',
             'Data Processing Agreement (DPA) + LOPGDG protocol',
             'Cyber liability insurance (€2M)',
             'Client portal + monthly report',
             'Remote helpdesk (business hours)'];
    if(isES)f1=['M365 BP — email, MFA, Conditional Access, Defender','Backup MSP360 en la nube — cifrado, externo','Backup de email (Dropsuite) — todos los buzones','Acuerdo DPA + protocolo LOPGDG','Seguro responsabilidad cibernética (€2M)','Portal de cliente + informe mensual','Helpdesk remoto (horario laboral)'];

    var f2=f1.concat(['FortiGate 60F Firewall — AI threat intel, IPS, VLAN, VPN',
                       'SolarWinds 24/7 RMM monitoring — auto patching',
                       'Quarterly Business Review (on-site)',
                       'Continual Improvement Register']);
    if(isES)f2=f1.concat(['FortiGate 60F Firewall — inteligencia artificial, IPS, VLAN','SolarWinds 24/7 RMM — monitoreo y parches automáticos','Revisión Trimestral de Negocio (presencial)','Registro de Mejora Continua']);

    var f3=f2.concat(['Dell T150 Server — RAID-1, centralized files, TrueNAS',
                       'Datto SIRIS 5 (2TB SSD) — instant cloud virtualization',
                       'APC UPS 1500VA — 30min runtime',
                       'SentinelOne Complete — AI EDR, zero-day, ransomware <1s',
                       'Annual compliance review — DPO advisory, LOPGDG gap']);
    if(isES)f3=f2.concat(['Servidor Dell T150 — RAID-1, archivos centralizados','Datto SIRIS 5 — virtualización en la nube instantánea','APC UPS 1500VA — 30min autonomía','SentinelOne Complete — EDR IA, zero-day','Revisión anual de cumplimiento — DPO']);

    var cards='<div class="pp-body"><div class="ps">'+
      '<h2 class="ps-title">'+(isES?'Tres Niveles':'Three Tiers')+'</h2><div class="tc">';
    [{t:d.t1,f:f1,name:L==='en'?'Essential':'Esencial',tag:L==='en'?'Sleep at night':'Duerme tranq.'},
     {t:d.t2,f:f2,name:L==='en'?'Professional':'Profesional',tag:L==='en'?'Sleep well':'Duerme bien'},
     {t:d.t3,f:f3,name:L==='en'?'Enterprise':'Empresarial',tag:L==='en'?'Zero worries':'Cero preocup.'}].forEach(function(cd,i){
      var isRec=(i+1)===rec;
      cards+='<div class="tcard'+(isRec?' rec':'')+'">';
      if(isRec)cards+='<div style="position:absolute;top:-9px;left:50%;transform:translateX(-50%);background:#DEDBC8;color:#0a0a0a;font-size:9px;font-weight:700;padding:3px 10px;border-radius:8px;">RECOMENDADO</div>';
      cards+='<div class="tc-name">'+cd.name+'</div><div class="tc-tag">'+cd.tag+'</div>'+
        '<div class="tc-price"><span class="tc-pa">€'+cd.t.mo+'</span> <span class="tc-pp">'+t('perMonth')+'</span></div>'+
        '<div class="tc-once">'+t('oneTime')+': €'+cd.t.ot+'</div>'+
        '<ul class="tier-card-features">';
      cd.f.forEach(function(feat){cards+='<li class="yes">'+feat+'</li>';});
      cards+='</ul></div>';
    });
    cards+='</div></div></div>';
    page(cards);

    // ROI
    page('<div class="pp-body"><div class="ps"><h2 class="ps-title">'+t('roi')+'</h2>'+
      '<div class="roi-section">'+
      '<div class="roi-card without"><h4>'+t('without')+'</h4>'+
      '<ul><li>'+(isES?'Recuperación de datos':'Data recovery')+': €2,000–€10,000</li>'+
      '<li>'+(isES?'Multa LOPDGD':'LOPDGD fine')+': €10,000–€600,000</li></ul></div>'+
      '<div class="roi-card with"><h4>'+t('withProtection')+'</h4>'+
      '<ul><li>'+(isES?'Pérdida cero':'Zero data loss')+' ✓</li><li>'+(isES?'Recuperación <1hr':'Recovery <1hr')+' ✓</li></ul></div>'+
      '</div></div></div>');

    // FOOTER
    page('<div class="pp-body"><div class="ns">'+
      '<h4>'+t('nextStep')+'</h4><p>'+t('nextStepTxt')+'</p>'+
      '<a href="#" class="ns-btn" onclick="window.print();return false;">'+(isES?'Descargar PDF':'Download PDF')+'</a>'+
      '</div></div>');

    // INTERNAL BRIEF
    var ib=document.getElementById('internalBrief');
    ib.innerHTML='';
    function ibS(h){ib.insertAdjacentHTML('beforeend','<div class="ib-sec">'+h+'</div>');}
    ibS('<div class="ib-hdr"><h2>'+t('intTitle')+': '+co+'</h2><p>'+d.rules.en+' | '+d.u+' users | '+d.dev+' devices</p></div>');

    function cTbl(t,name){
      var mb=t.m>30?'mb-g':t.m>15?'mb-o':'mb-r';
      ibS('<h3>'+t('costBreak')+' — '+name+'</h3>'+
        '<table class="ct"><thead><tr><th>'+t('module')+'</th><th class="num">'+t('ourCost')+'</th><th class="num">'+t('clientPays')+'</th><th class="num">'+t('margin')+'</th></tr></thead><tbody>'+
        '<tr><td>All modules + labor</td><td class="num">€'+Math.round(t.cm)+'</td><td class="num">€'+t.mo+'</td><td class="num">'+t.m+'%</td></tr>'+
        '<tr><td>One-time</td><td class="num">€'+t.ct+'</td><td class="num">€'+t.ot+'</td><td>—</td></tr>'+
        '<tr class="tot"><td>'+t('total')+' (Y1)</td><td class="num">€'+t.yc+'</td><td class="num">€'+t.yr+'</td><td><span class="mb '+mb+'">'+t.m+'%</span></td></tr>'+
        '<tr class="tot '+(t.p>0?'prof':'loss')+'"><td colspan="2">'+t('profit')+'</td><td colspan="2" style="text-align:right;">€'+t.p+'</td></tr>'+
        '</tbody></table>');
    }
    cTbl(d.t1,isES?'T1: Esencial':'T1: Essential');
    cTbl(d.t2,isES?'T2: Profesional':'T2: Professional');
    cTbl(d.t3,isES?'T3: Empresarial':'T3: Enterprise');

    // WORKFLOW
    ibS('<h3>'+t('wfTitle')+'</h3>'+
      '<div class="workflow-steps">'+
      '<div class="step"><div class="step-num">1</div><div><strong>'+(isES?'Instalación Remota':'Remote Setup')+'</strong><br><span>'+(isES?'Configurar M365, MFA, backup policies, Dropsuite':'Configure M365, MFA, backup policies, Dropsuite')+'</span></div></div>'+
      '<div class="step"><div class="step-num">2</div><div><strong>'+(isES?'Visita On-Site':'On-Site Visit')+'</strong><br><span>'+(isES?'Instalar agentes, verificar backups, formación':'Deploy agents, verify backups, training')+'</span></div></div>'+
      '<div class="step"><div class="step-num">3</div><div><strong>'+(isES?'NOC Toma Control':'NOC Takes Over')+'</strong><br><span>'+(isES?'Monitoreo 24/7 activo, primer reporte enviado':'24/7 monitoring active, first report sent')+'</span></div></div>'+
      '</div>');

    btn.disabled=false;btn.textContent=t('btn_gen');
  },50);
}
updateLabels();
