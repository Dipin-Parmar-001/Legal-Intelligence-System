import streamlit as st

st.set_page_config(
    page_title="LexAI · Legal Research",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

:root {
    --bg:        #f7f5ff;
    --white:     #ffffff;
    --indigo:    #4f35d2;
    --indigo2:   #6c52e8;
    --violet:    #7c3aed;
    --teal:      #0d9488;
    --amber:     #d97706;
    --rose:      #e11d48;
    --ink:       #12102a;
    --ink2:      #2e2a4a;
    --ink3:      #6b6880;
    --card:      #ffffff;
    --border:    #e5e0fa;
    --border2:   #cdc8f5;
    --grad1:     linear-gradient(135deg, #4f35d2 0%, #7c3aed 100%);
    --grad2:     linear-gradient(135deg, #0d9488 0%, #059669 100%);
    --grad3:     linear-gradient(135deg, #d97706 0%, #ea580c 100%);
    --grad-hero: linear-gradient(135deg, #4f35d2 0%, #6c52e8 40%, #7c3aed 100%);
    --shadow-sm: 0 2px 8px rgba(79,53,210,0.10);
    --shadow-md: 0 8px 32px rgba(79,53,210,0.15);
    --shadow-lg: 0 20px 60px rgba(79,53,210,0.20);
}

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background: var(--bg) !important;
    color: var(--ink) !important;
}
.stApp { background: var(--bg) !important; }
.block-container { padding: 0 2rem 5rem !important; max-width: 1280px !important; }
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ══════════ HERO ══════════ */
.hero-wrap {
    background: var(--grad-hero);
    margin: 0 -2rem 2.5rem;
    padding: 3rem 3rem 2.5rem;
    position: relative;
    overflow: hidden;
}
.hero-wrap::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 80% 20%, rgba(255,255,255,0.12) 0%, transparent 50%),
        radial-gradient(circle at 10% 90%, rgba(124,58,237,0.4) 0%, transparent 50%);
}
.hero-dots {
    position: absolute;
    top: 20px; right: 80px;
    width: 160px; height: 160px;
    opacity: 0.12;
    background-image: radial-gradient(circle, white 1.5px, transparent 1.5px);
    background-size: 18px 18px;
}
.hero-ring {
    position: absolute;
    bottom: -60px; right: -40px;
    width: 240px; height: 240px;
    border-radius: 50%;
    border: 32px solid rgba(255,255,255,0.08);
}
.hero-inner { position: relative; z-index: 1; }
.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 100px;
    padding: 0.3rem 0.9rem;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.9);
    margin-bottom: 1rem;
    backdrop-filter: blur(8px);
}
.hero-dot { width: 6px; height: 6px; background: #a5f3fc; border-radius: 50%; animation: ping 2s ease infinite; }
@keyframes ping { 0%,100%{transform:scale(1);opacity:1;} 50%{transform:scale(1.6);opacity:0.5;} }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 3.4rem;
    color: #fff;
    line-height: 1.05;
    letter-spacing: -0.03em;
    margin-bottom: 0.75rem;
}
.hero-title em {
    font-style: normal;
    background: linear-gradient(90deg, #a5f3fc, #c4b5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 1rem;
    color: rgba(255,255,255,0.72);
    font-weight: 400;
    line-height: 1.6;
    max-width: 480px;
}
.hero-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1.5rem;
}
.hero-chip {
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.22);
    border-radius: 100px;
    padding: 0.3rem 0.85rem;
    font-size: 0.78rem;
    font-weight: 600;
    color: rgba(255,255,255,0.88);
    cursor: default;
    backdrop-filter: blur(4px);
    transition: all 0.2s;
}
.hero-chip:hover {
    background: rgba(255,255,255,0.22);
    color: #fff;
    transform: translateY(-1px);
}

/* ══════════ SECTION LABEL ══════════ */
.sec-head {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 0.9rem;
}
.sec-icon {
    width: 28px; height: 28px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.85rem;
    flex-shrink: 0;
}
.sec-icon.purple { background: linear-gradient(135deg,#ede9fe,#ddd6fe); }
.sec-icon.teal   { background: linear-gradient(135deg,#ccfbf1,#99f6e4); }
.sec-label-text {
    font-family: 'Syne', sans-serif;
    font-size: 0.8rem;
    font-weight: 800;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--ink3);
}

/* ══════════ INPUT CARD ══════════ */
.input-card {
    background: var(--white);
    border-radius: 20px;
    border: 1.5px solid var(--border);
    padding: 1.5rem;
    box-shadow: var(--shadow-sm);
    margin-bottom: 1rem;
}
.stTextArea textarea {
    background: var(--bg) !important;
    border: 2px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--ink) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.96rem !important;
    font-weight: 500 !important;
    padding: 0.9rem 1rem !important;
    transition: all 0.2s !important;
    resize: vertical !important;
    line-height: 1.6 !important;
}
.stTextArea textarea:focus {
    border-color: var(--indigo) !important;
    background: #fff !important;
    box-shadow: 0 0 0 4px rgba(79,53,210,0.10) !important;
    outline: none !important;
}
.stTextArea textarea::placeholder { color: var(--ink3) !important; font-style: italic !important; font-weight: 400 !important; }

/* ══════════ BUTTONS ══════════ */
.stButton > button {
    background: var(--grad1) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.72rem 1.6rem !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    letter-spacing: 0.01em !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 16px rgba(79,53,210,0.35) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(79,53,210,0.45) !important;
    filter: brightness(1.08) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* Clear button override */
div[data-testid="column"]:nth-child(2) .stButton > button {
    background: var(--white) !important;
    color: var(--ink3) !important;
    border: 1.5px solid var(--border2) !important;
    box-shadow: none !important;
}
div[data-testid="column"]:nth-child(2) .stButton > button:hover {
    background: var(--bg) !important;
    color: var(--ink) !important;
    border-color: var(--indigo) !important;
    box-shadow: none !important;
}

/* ══════════ PIPELINE ══════════ */
.pipe-wrap {
    background: var(--white);
    border-radius: 20px;
    border: 1.5px solid var(--border);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
}
.pipe-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem 1.2rem;
    border-bottom: 1px solid var(--border);
    transition: all 0.25s;
    position: relative;
}
.pipe-item:last-child { border-bottom: none; }
.pipe-item.active {
    background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
    border-left: 3px solid var(--indigo);
}
.pipe-item.done {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border-left: 3px solid var(--teal);
}
.pipe-item.pending { border-left: 3px solid transparent; }

.pipe-orb {
    width: 40px; height: 40px;
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
    transition: all 0.25s;
}
.pipe-orb.pending { background: #f1f0f9; }
.pipe-orb.active  { background: var(--grad1); box-shadow: 0 4px 14px rgba(79,53,210,0.35); }
.pipe-orb.done    { background: var(--grad2); box-shadow: 0 4px 14px rgba(13,148,136,0.30); }

.pipe-info { flex: 1; }
.pipe-name {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 0.88rem;
    color: var(--ink);
    margin-bottom: 0.15rem;
}
.pipe-desc {
    font-size: 0.74rem;
    color: var(--ink3);
    font-weight: 400;
    line-height: 1.4;
}

.pipe-badge {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 0.2rem 0.65rem;
    border-radius: 100px;
    flex-shrink: 0;
}
.badge-pending { background: #f1f0f9; color: var(--ink3); }
.badge-active  { background: var(--indigo); color: #fff; animation: pulse-badge 1.5s ease infinite; }
.badge-done    { background: var(--teal); color: #fff; }
@keyframes pulse-badge { 0%,100%{opacity:1;} 50%{opacity:0.65;} }

/* ══════════ RESULT TABS ══════════ */
.stTabs [data-baseweb="tab-list"] {
    background: #ede9fe !important;
    border-radius: 14px 14px 0 0 !important;
    border: none !important;
    padding: 0.35rem 0.35rem 0 !important;
    gap: 0.2rem !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--ink3) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.04em !important;
    border-radius: 10px 10px 0 0 !important;
    padding: 0.55rem 1.1rem !important;
    transition: all 0.2s !important;
}
.stTabs [aria-selected="true"] {
    background: var(--white) !important;
    color: var(--indigo) !important;
    box-shadow: 0 -2px 8px rgba(79,53,210,0.08) !important;
}
.stTabs [data-baseweb="tab-panel"] { padding: 0 !important; }

/* ══════════ RESULT PANELS ══════════ */
.result-card {
    background: var(--white);
    border: 1.5px solid var(--border);
    border-top: none;
    border-radius: 0 0 18px 18px;
    overflow: hidden;
}
.result-body {
    padding: 1.4rem 1.6rem;
    font-size: 0.88rem;
    line-height: 1.85;
    color: var(--ink2);
    white-space: pre-wrap;
    font-weight: 400;
    max-height: 430px;
    overflow-y: auto;
}
.result-body::-webkit-scrollbar { width: 4px; }
.result-body::-webkit-scrollbar-track { background: transparent; }
.result-body::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }

/* ══════════ FINAL ANSWER ══════════ */
.final-card {
    background: var(--white);
    border: 1.5px solid var(--border);
    border-top: none;
    border-radius: 0 0 18px 18px;
    overflow: hidden;
}
.final-banner {
    background: linear-gradient(135deg, #052e16 0%, #14532d 100%);
    padding: 1rem 1.4rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}
.final-banner-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 0.95rem;
    color: #fff;
    flex: 1;
    letter-spacing: 0.01em;
}
.verified-tag {
    background: #16a34a;
    color: #fff;
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.2rem 0.65rem;
    border-radius: 100px;
}
.final-body {
    padding: 1.5rem 1.6rem;
    font-size: 0.9rem;
    line-height: 1.9;
    color: var(--ink);
    white-space: pre-wrap;
    font-weight: 500;
    max-height: 440px;
    overflow-y: auto;
}
.final-body::-webkit-scrollbar { width: 4px; }
.final-body::-webkit-scrollbar-track { background: transparent; }
.final-body::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }

/* ══════════ QUERY STRIP ══════════ */
.query-strip {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    background: linear-gradient(135deg, #f5f3ff, #ede9fe);
    border: 1.5px solid var(--border2);
    border-radius: 14px;
    padding: 0.85rem 1.1rem;
    margin-bottom: 1rem;
}
.query-strip-icon {
    width: 32px; height: 32px;
    background: var(--grad1);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.9rem;
    flex-shrink: 0;
    box-shadow: 0 3px 10px rgba(79,53,210,0.3);
}
.query-strip-label {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--indigo);
    margin-bottom: 0.2rem;
}
.query-strip-text {
    font-size: 0.88rem;
    font-weight: 600;
    color: var(--ink);
    line-height: 1.5;
}

/* ══════════ EMPTY STATE ══════════ */
.empty-card {
    background: var(--white);
    border: 2px dashed var(--border2);
    border-radius: 20px;
    padding: 3.5rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.empty-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 40%, rgba(79,53,210,0.04) 0%, transparent 70%);
}
.empty-glyph {
    font-size: 3.5rem;
    margin-bottom: 0.75rem;
    display: block;
    animation: float 3s ease-in-out infinite;
}
@keyframes float { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-8px);} }
.empty-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.1rem;
    color: var(--ink2);
    margin-bottom: 0.4rem;
}
.empty-sub { font-size: 0.82rem; color: var(--ink3); font-weight: 400; }

/* ══════════ STATS ROW ══════════ */
.stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.75rem;
    margin-bottom: 1rem;
}
.stat-card {
    background: var(--white);
    border: 1.5px solid var(--border);
    border-radius: 14px;
    padding: 0.9rem 1rem;
    text-align: center;
    transition: all 0.2s;
}
.stat-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-sm); }
.stat-num {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.5rem;
    background: var(--grad1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
}
.stat-lbl { font-size: 0.68rem; font-weight: 600; color: var(--ink3); margin-top: 0.2rem; text-transform: uppercase; letter-spacing: 0.08em; }

/* ══════════ SPINNER ══════════ */
.stSpinner > div { border-top-color: var(--indigo) !important; }
</style>
""", unsafe_allow_html=True)

# ── Session State ──────────────────────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []
if "total_queries" not in st.session_state:
    st.session_state.total_queries = 0

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
    <div class="hero-dots"></div>
    <div class="hero-ring"></div>
    <div class="hero-inner">
        <div class="hero-eyebrow">
            <div class="hero-dot"></div>
            AI-Powered · Indian Legal Research
        </div>
        <div class="hero-title">Your AI <em>Legal</em><br>Research Assistant</div>
        <div class="hero-sub">Multi-agent pipeline that searches, drafts, and verifies legal answers — grounded in real sources.</div>
        <div class="hero-chips">
            <span class="hero-chip">⚖️ Supreme Court</span>
            <span class="hero-chip">📜 Constitution</span>
            <span class="hero-chip">🔍 Case Law</span>
            <span class="hero-chip">🏛️ High Courts</span>
            <span class="hero-chip">📋 IPC / CrPC</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── COLUMNS ───────────────────────────────────────────────────────────────────
left, right = st.columns([1, 1.15], gap="large")

# ══ LEFT ══════════════════════════════════════════════════════════════════════
with left:

    # Stats row
    st.markdown(f"""
    <div class="stats-row">
        <div class="stat-card">
            <div class="stat-num">{st.session_state.total_queries}</div>
            <div class="stat-lbl">Researched</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">3</div>
            <div class="stat-lbl">AI Agents</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">6+</div>
            <div class="stat-lbl">Sources/Query</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Input
    st.markdown("""
    <div class="sec-head">
        <div class="sec-icon purple">🔍</div>
        <span class="sec-label-text">Ask a Legal Question</span>
    </div>
    """, unsafe_allow_html=True)

    query = st.text_area(
        label="q",
        label_visibility="collapsed",
        placeholder="e.g. What are the latest Supreme Court rulings on anticipatory bail in 2025?",
        height=120,
        key="query_input",
    )

    b1, b2 = st.columns([5, 2])
    with b1:
        run = st.button("⚡  Research Now", use_container_width=True)
    with b2:
        if st.button("Clear", use_container_width=True) and st.session_state.history:
            st.session_state.history = []
            st.rerun()

    st.markdown("<div style='height:1.4rem'></div>", unsafe_allow_html=True)

    # Pipeline
    st.markdown("""
    <div class="sec-head">
        <div class="sec-icon teal">⚙️</div>
        <span class="sec-label-text">Pipeline Status</span>
    </div>
    """, unsafe_allow_html=True)

    stage_ph = st.empty()

    def render_stages(active=None, done=None):
        done = done or []
        stages = [
            ("🔎", "Search Agent",    "Web search · recency check · source grounding"),
            ("✍️", "Writer Agent",    "Structured legal drafting from research"),
            ("🔬", "Corrector Agent", "Fact-check · hallucination removal · logic"),
        ]
        html = '<div class="pipe-wrap">'
        for i, (icon, name, desc) in enumerate(stages):
            if i in done:
                item_cls, orb_cls, badge = "done",    "done",    '<span class="pipe-badge badge-done">✓ Done</span>'
            elif i == active:
                item_cls, orb_cls, badge = "active",  "active",  '<span class="pipe-badge badge-active">Running…</span>'
            else:
                item_cls, orb_cls, badge = "pending", "pending", '<span class="pipe-badge badge-pending">Waiting</span>'
            html += f"""
            <div class="pipe-item {item_cls}">
                <div class="pipe-orb {orb_cls}">{icon}</div>
                <div class="pipe-info">
                    <div class="pipe-name">{name}</div>
                    <div class="pipe-desc">{desc}</div>
                </div>
                {badge}
            </div>"""
        html += '</div>'
        stage_ph.markdown(html, unsafe_allow_html=True)

    render_stages()

# ══ RIGHT ═════════════════════════════════════════════════════════════════════
with right:
    st.markdown("""
    <div class="sec-head">
        <div class="sec-icon purple">📋</div>
        <span class="sec-label-text">Research Output</span>
    </div>
    """, unsafe_allow_html=True)

    result_ph = st.empty()

    def show_empty():
        result_ph.markdown("""
        <div class="empty-card">
            <span class="empty-glyph">⚖️</span>
            <div class="empty-title">Ready to Research</div>
            <div class="empty-sub">Type your legal question on the left and hit Research Now.<br>Your verified answer will appear here.</div>
        </div>
        """, unsafe_allow_html=True)

    def show_results(rec):
        with result_ph.container():
            st.markdown(f"""
            <div class="query-strip">
                <div class="query-strip-icon">💬</div>
                <div>
                    <div class="query-strip-label">Your Question</div>
                    <div class="query-strip-text">{rec['query']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            tabs = st.tabs(["✅ Final Answer", "🔍 Research Bundle", "✍️ Draft"])
            with tabs[0]:
                st.markdown(f"""
                <div class="final-card">
                    <div class="final-banner">
                        <span>✅</span>
                        <span class="final-banner-title">Verified Legal Answer</span>
                        <span class="verified-tag">Verified</span>
                    </div>
                    <div class="final-body">{rec['final']}</div>
                </div>
                """, unsafe_allow_html=True)
            with tabs[1]:
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-body">{rec['search']}</div>
                </div>
                """, unsafe_allow_html=True)
            with tabs[2]:
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-body">{rec['draft']}</div>
                </div>
                """, unsafe_allow_html=True)

    if st.session_state.history:
        show_results(st.session_state.history[-1])
    else:
        show_empty()

# ══ RUN ═══════════════════════════════════════════════════════════════════════
if run and query.strip():
    st.session_state.total_queries += 1

    with left:
        render_stages(active=0)
    with right:
        result_ph.markdown("""
        <div class="empty-card">
            <span class="empty-glyph">🔍</span>
            <div class="empty-title">Searching the web…</div>
            <div class="empty-sub">Gathering real sources and recent case law.</div>
        </div>
        """, unsafe_allow_html=True)

    try:
        from agents import writer_chain, corrector_chain, search_agent

        searcher = search_agent()
        sr = searcher.invoke({"messages": [("user", query)]})
        search_text = sr["messages"][-1].content

        with left: render_stages(active=1, done=[0])
        with right:
            result_ph.markdown("""
            <div class="empty-card">
                <span class="empty-glyph">✍️</span>
                <div class="empty-title">Drafting your answer…</div>
                <div class="empty-sub">Structuring findings into a legal brief.</div>
            </div>
            """, unsafe_allow_html=True)

        writer_out = writer_chain.invoke({"content": search_text})
        draft_text = writer_out.content

        with left: render_stages(active=2, done=[0, 1])
        with right:
            result_ph.markdown("""
            <div class="empty-card">
                <span class="empty-glyph">🔬</span>
                <div class="empty-title">Verifying & correcting…</div>
                <div class="empty-sub">Removing errors, checking facts, tightening logic.</div>
            </div>
            """, unsafe_allow_html=True)

        corrector_out = corrector_chain.invoke({"data": draft_text})
        final_text = corrector_out.content

        with left: render_stages(done=[0, 1, 2])

        rec = {"query": query, "search": search_text, "draft": draft_text, "final": final_text}
        st.session_state.history.append(rec)

        with right:
            show_results(rec)

    except ImportError as e:
        with right:
            result_ph.error(f"**Import error** — make sure `agents.py` & `tools.py` are in the same folder.\n\n`{e}`")
        with left:
            render_stages()

elif run and not query.strip():
    st.warning("⚠️ Please enter a legal question before running.")