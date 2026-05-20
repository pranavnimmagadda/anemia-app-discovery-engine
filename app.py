import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="AI Anemia Capital & Marketing Discovery Engine",
    page_icon="🩸",
    layout="wide"
)

# ----------------------------------------------------
# 1. ENRICHED ALGORITHMIC SCORING ENGINE
# ----------------------------------------------------
def calculate_alignment_score(title, description):
    """
    Calculates exact alignment weights based on your deep learning stack, 
    clinical targeting, and physical smartphone image artifacts.
    """
    text = f"{title} {description}".lower()
    score = 0
    
    # Tier 1 (Weight: +3) - Core Anemia & Microvascular Tissue Tracking
    tier1_critical = [
        "non-invasive", "hemoglobin", "anemia", "palpebral", "conjunctiva", 
        "pallor", "point-of-care", "triage", "maternal health", "screening tool"
    ]
    # Tier 2 (Weight: +2) - CV Architecture & Smartphone Artifacts
    tier2_technical = [
        "computer vision", "deep learning", "efficientnet", "segmentation mask", 
        "image processing", "opencv", "glare", "specular reflection", 
        "camera calibration", "gaze tracking", "mhealth", "low-resource settings"
    ]
    # Tier 3 (Weight: +1) - Broad Market & Impact Areas
    tier3_broad = [
        "digital health", "medtech", "diagnostics", "health equity", "biomanufacturing"
    ]
    
    for word in tier1_critical:
        if word in text: score += 3
    for word in tier2_technical:
        if word in text: score += 2
    for word in tier3_broad:
        if word in text: score += 1
            
    return min(score, 10)

# ----------------------------------------------------
# 2. SEED DATA: LIVE 2026 TOP-TIER OPPORTUNITIES
# ----------------------------------------------------
if 'opportunities' not in st.session_state:
    preset_data = [
        {
            "id": 1,
            "name": "Grand Challenges India (GCI): Breakthrough Solutions for Screening & Diagnosis",
            "category": "Grant (Non-Dilutive)",
            "value": "Up to ₹2 Crore (USD 200,000) for Product-oriented tracks",
            "deadline": datetime.date(2026, 7, 1),
            "description": "Joint open call by GCI-BIRAC and the Gates Foundation. Explicitly targets high-risk, high-reward diagnostic innovations, software-defined diagnostics, and AI-enabled screening tools that drive zero or ultra-low incremental costs in decentralized healthcare networks.",
            "status": "Not Started",
            "artifacts": ["Technical Abstract", "Budget Breakdown", "Clinical Feasibility Study"]
        },
        {
            "id": 2,
            "name": "SAMRIDH Impact Accelerator Program",
            "category": "Grant (Non-Dilutive)",
            "value": "Up to ₹40 Lakh Matching Funding + Scaling Access",
            "deadline": datetime.date(2026, 6, 15),
            "description": "MeitY Startup Hub initiative tailored for digital technology and product-focused deeptech software startups solving critical social impact problems in healthcare. Focuses on moving software solutions from MVP to scale in tier-2/3 resource-constrained networks.",
            "status": "Not Started",
            "artifacts": ["5-Min Pitch Deck", "Financial Model", "DPIIT Certificate"]
        },
        {
            "id": 3,
            "name": "Startup Prize: Health 2026 Competition",
            "category": "Pitch Competition",
            "value": "$25,000 Cash + Global Venture Network",
            "deadline": datetime.date(2026, 6, 15),
            "description": "Prominent international startup track splitting companies into FDA and Non-FDA paths. Perfectly tailored for mobile screening apps and software-as-a-service diagnostic tools handling consumer health metrics.",
            "status": "Not Started",
            "artifacts": ["5-Min Pitch Deck", "Video Demo"]
        },
        {
            "id": 4,
            "name": "MICCAI 2026: OMIA (Ophthalmic Medical Image Analysis Workshop)",
            "category": "Academic Conference",
            "value": "Peer-reviewed Publication & Global Exposure",
            "deadline": datetime.date(2026, 6, 1),
            "description": "The premier international deep-learning conference track for structural eye region and eyelid segmentation models. Highly relevant for validating custom segmentation boundaries and artifact management algorithms.",
            "status": "Drafting Abstract",
            "artifacts": ["Technical Abstract"]
        }
    ]
    
    for item in preset_data:
        item["score"] = calculate_alignment_score(item["name"], item["description"])
    st.session_state.opportunities = preset_data

# ----------------------------------------------------
# 3. INTERFACE HEADER & METRICS
# ----------------------------------------------------
st.title("🩸 AI Anemia Application: Capital & Marketing Discovery Engine")
st.markdown("Automated algorithmic curation framework for non-dilutive grant funding, pitch opportunities, and conference exposure tracks.")
st.markdown("---")

df = pd.DataFrame(st.session_state.opportunities)

m1, m2, m3 = st.columns(3)
m1.metric("Total Active Tracks", len(df))
m2.metric("High Priority (>6 Score)", len(df[df['score'] >= 6]))
m3.metric("Pending Nearest Deadline", str(df['deadline'].min()))

# ----------------------------------------------------
# 4. SIDEBAR: DATA COLLECTION PORTAL
# ----------------------------------------------------
st.sidebar.header("📥 Ingest New Opportunity")
with st.sidebar.form("ingest_form", clear_on_submit=True):
    new_name = st.text_input("Opportunity Name", placeholder="e.g., BIRAC BIG Grant")
    new_cat = st.selectbox("Category", ["Grant (Non-Dilutive)", "Pitch Competition", "Academic Conference", "Industry Expo"])
    new_val = st.text_input("Funding / Prize Value", placeholder="e.g., Equity-free cash, Grant allocation")
    new_dl = st.date_input("Submission Deadline", datetime.date.today() + datetime.timedelta(days=30))
    new_desc = st.text_area("Scope Description", placeholder="Paste submission requirements, evaluation criteria, or target objectives here...")
    new_art = st.multiselect("Required Submission Artifacts", ["Technical Abstract", "5-Min Pitch Deck", "Video Demo", "Budget Breakdown", "Clinical Feasibility Study", "Proof of Concept Data"])
    
    submit_btn = st.form_submit_with_button("Run Analysis Pipeline")

if submit_btn and new_name and new_desc:
    calc_score = calculate_alignment_score(new_name, new_desc)
    new_entry = {
        "id": len(st.session_state.opportunities) + 1,
        "name": new_name,
        "category": new_cat,
        "value": new_val,
        "deadline": new_dl,
        "description": new_desc,
        "status": "Not Started",
        "artifacts": new_art,
        "score": calc_score
    }
    st.session_state.opportunities.append(new_entry)
    st.sidebar.success(f"Opportunity Evaluated! Triage Score: {calc_score}/10")

# ----------------------------------------------------
# 5. CORE PIPELINE VIEW
# ----------------------------------------------------
st.subheader("📋 Execution Tracker")
col_f1, col_f2 = st.columns(2)
with col_f1:
    filter_cat = st.multiselect("Filter by Category", options=df['category'].unique(), default=df['category'].unique())
with col_f2:
    filter_status = st.multiselect("Filter by Pipeline Status", options=df['status'].unique(), default=df['status'].unique())

filtered_df = df[(df['category'].isin(filter_cat)) & (df['status'].isin(filter_status))].sort_values(by="deadline")

for idx, row in filtered_df.iterrows():
    with st.container():
        score_color = "🔴" if row['score'] >= 7 else "🟡" if row['score'] >= 4 else "⚪"
        
        c1, c2, c3, c4 = st.columns([2, 1, 1, 1])
        with c1:
            st.markdown(f"### {score_color} {row['name']}")
            st.caption(f"**Description:** {row['description']}")
        with c2:
            st.markdown(f"**Value:**\n`{row['value']}`")
            st.markdown(f"**Deadline:**\n`{str(row['deadline'])}`")
        with c3:
            st.markdown(f"**Triage Score:**\n`{row['score']} / 10`")
            st.markdown(f"**Type:** `{row['category']}`")
        with c4:
            current_status_idx = ["Not Started", "Drafting Abstract", "Under Review", "Accepted", "Rejected"].index(row['status'])
            new_status = st.selectbox(f"Status Update (ID:{row['id']})", ["Not Started", "Drafting Abstract", "Under Review", "Accepted", "Rejected"], index=current_status_idx, key=f"status_{row['id']}")
            if new_status != row['status']:
                st.session_state.opportunities[row['id']-1]['status'] = new_status
                st.rerun()
                
        st.markdown(f"**Required Deliverables Checklist:** {', '.join([f'• {art}' for art in row['artifacts']]) if row['artifacts'] else 'None marked'}")
        st.markdown("---")

# ----------------------------------------------------
# 6. ASSET MANIFEST & TAILORED BOILERPLATES
# ----------------------------------------------------
st.subheader("📝 Dynamic Application Generator")
st.markdown("Select an opportunity to compile technical messaging aligned with your segmentation models and image cleanup processes.")

selected_opp_name = st.selectbox("Target Opportunity Matrix", options=df['name'].unique())
selected_opp = df[df['name'] == selected_opp_name].iloc[0]

tab1, tab2, tab3 = st.tabs(["Grant Technical Proposal", "Startup Pitch Deck Voice", "Academic Peer-Review Abstract"])

with tab1:
    st.markdown("> **Target Deployment:** High-fit text blocks for Grant Applications, Innovation statements, and Medical Device submissions.")
    st.code(f"""
PROJECT APPLICATION PROFILE: {selected_opp['name']}
CORE ARCHITECTURE TARGET: Non-Invasive AI Hemoglobin Estimation via Automated Palpebral Conjunctiva Segmentation

EXECUTIVE SUMMARY & DISRUPTION PROPOSAL:
Nutritional anemia represents a critical public health vector, directly compounding maternal and pediatric risk profiles in lower-and-middle-income countries (LMICs). Standard diagnosis requires invasive blood draws, specialized technicians, cold-chain infrastructure, and expensive consumable reagents. 

We propose an engineering-led software alternative: a smartphone-based point-of-care tool designed to deliver high-precision triage at zero incremental cost per use. Built upon a native Python and OpenCV stack, our technology utilizes an EfficientNet B3 neural network architecture optimized to automatically generate structural segmentation masks of the palpebral conjunctiva. By analyzing sub-surface tissue color distribution metrics and localized microvascular pallor indices, the software computes rapid hemoglobin estimations.

To address unconstrained environmental anomalies (such as specular reflections, ambient lux fluctuations, and variable user positioning), our pipeline features a dual-stage upstream calibration module: (1) a spatial camera calibration engine to match lens parameters, and (2) an automated real-time gaze verification tracking loop. This system actively mitigates glare-induced artifacts and border under-segmentation, delivering robust, laboratory-grade performance across consumer hardware.
    """, language="text")

with tab2:
    st.markdown("> **Target Deployment:** 3-5 Minute Pitch Competitions, Venture Accelerator Panels, and Marketing materials.")
    st.code(f"""
PITCH TRACK DESIGNED FOR: {selected_opp['name']}

THE PROBLEM: Anemia affects over 1.6 billion people globally, but the diagnostic system is broken. Screening still depends on painful needles, chemical supplies, biohazard waste, and clinical logistics that don't reach low-resource populations.

THE SOLUTION: We turn any standard smartphone into an instant, needle-free hemoglobin screening portal. By taking a 2-second image of the lower eyelid, our deep learning engine automatically targets the palpebral conjunctiva tissue, quantifies microvascular blood pallor, and estimates hemoglobin values in under 30 seconds.

COMMERCIAL & ARCHITECTURAL MOAT:
Unlike basic filters, our enterprise software is built for field-level friction. Powered by an EfficientNet B3 deep neural network framework and OpenCV morphological cleanup layers, our core application includes an integrated gaze-detection loop and automated hardware calibration matrix. We systematically isolate and eliminate the reflections, user handling variances, and glare anomalies that cripple generic computer vision applications. Pressure-tested and validated across an audit of 118 distinct clinical image profiles, our engine delivers an ultra-stable triage mechanism built to scale infinitely at near-zero incremental cost.
    """, language="text")

with tab3:
    st.markdown("> **Target Deployment:** Peer-reviewed Engineering Workshops, Call-For-Papers (CFP), and Conference Proceedings.")
    st.code(f"""
PROPOSED STUDY: Robust Palpebral Conjunctiva Segmentation and Ambient Artifact Mitigation Using EfficientNet B3 Architectures for Mobile Diagnostics

CONTEXTUAL SCOPE: {selected_opp['description']}

ABSTRACT TEXT BODY:
Deploying mobile deep learning structures for point-of-care clinical triage demands extreme algorithmic resilience against unconstrained, non-laboratory environments. This study introduces an optimized computer vision pipeline engineered for robust, automated palpebral conjunctiva segmentation to support non-invasive, colorimetric hemoglobin estimation.

The core framework details an EfficientNet B3 deep convolutional architecture integrated with custom morphological image processing passes in Python and OpenCV. To handle the primary failure vectors of consumer-smartphone medical imaging—specifically severe boundary under-segmentation caused by specular glare, variant ambient illumination, and inconsistent eye-gaze alignment—we deploy an integrated upstream preprocessing architecture consisting of: (1) a geometric camera calibration module to reconcile sensor variations, and (2) a real-time gaze-detection tracking loop to enforce precise tissue exposure limits before frame ingestion.

The consolidated model pipeline performance was evaluated and calibrated utilizing a technical audit of 118 distinct, highly variable clinical image files containing pronounced light and glare artifacts. The results demonstrate substantial performance gains in isolating regional target tissue fields, eliminating glare-induced structural fragmentation, and preserving a high mean Intersection over Union (mIoU) score requisite for precise microvascular colorimetric tissue analysis.
    """, language="text")
