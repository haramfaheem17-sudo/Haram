import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Textile Industry Dashboard",
    page_icon="🧵",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>
.stApp {
    background-color: #F4F8F7;
}

[data-testid="stSidebar"] {
    background-color: #E2EFEB;
}

.hero {
    padding: 25px;
    border-radius: 18px;
    color: white;
    background: linear-gradient(
        120deg, #123C3A, #1E7168, #68A89A
    );
    margin-bottom: 20px;
}

.hero h1 {
    margin: 0;
    font-size: 35px;
}

.hero p {
    font-size: 17px;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #D6E5E0;
    padding: 15px;
    border-radius: 14px;
}

</style>
""", unsafe_allow_html=True)


# Sidebar
st.sidebar.title("🧵 Textile Hub")
st.sidebar.write("Textile Industry Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Production Planner",
        "Fiber Guide",
        "About"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Color Palette")

st.sidebar.markdown("""
- 🟢 Deep Teal: #123C3A
- 🟢 Teal: #1E7168
- 🌿 Sage Green: #A8C9BD
- ⚪ Soft Cream: #F4F8F7
""")


# =========================
# OVERVIEW PAGE
# =========================

if page == "Overview":

    st.markdown("""
    <div class="hero">
        <h1>Textile Industry Dashboard</h1>
        <p>
        Explore textile production, fiber types,
        and manufacturing information.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Monthly Output", "12,500 m", "+6.2%")
    col2.metric("Fabric Orders", "248", "+12")
    col3.metric("Quality Pass Rate", "96.4%", "+1.1%")
    col4.metric("Waste Rate", "3.8%", "-0.5%")

    st.subheader("Monthly Production")

    chart_data = pd.DataFrame({
        "Month": ["May", "June", "July", "August", "September", "October"],
        "Cotton Fabric": [7200, 7600, 8100, 7900, 8600, 9000],
        "Blended Fabric": [3100, 3300, 3500, 3700, 3600, 3900]
    })

    chart_data = chart_data.set_index("Month")

    st.bar_chart(
        chart_data,
        color=["#1E7168", "#A8C9BD"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Textile Production Process")

        st.markdown("""
        1. Fiber Selection
        2. Spinning
        3. Yarn Production
        4. Weaving or Knitting
        5. Dyeing and Finishing
        6. Quality Testing
        7. Garment Manufacturing
        """)

    with col2:
        st.subheader("Quality Checklist")

        st.checkbox("Check fabric color")
        st.checkbox("Inspect fabric defects")
        st.checkbox("Check fabric width")
        st.checkbox("Record inspection results")


# =========================
# PRODUCTION PLANNER
# =========================

elif page == "Production Planner":

    st.markdown("""
    <div class="hero">
        <h1>Production Planner</h1>
        <p>Calculate fabric requirements and production time.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        order_meters = st.number_input(
            "Required Fabric (meters)",
            min_value=1,
            max_value=1000000,
            value=5000,
            step=100
        )

        daily_capacity = st.number_input(
            "Daily Production Capacity (meters)",
            min_value=1,
            max_value=100000,
            value=800,
            step=50
        )

        waste_percent = st.slider(
            "Estimated Waste (%)",
            min_value=0,
            max_value=20,
            value=4
        )

    with col2:

        fabric_type = st.selectbox(
            "Select Fabric Type",
            [
                "Cotton",
                "Polyester",
                "Cotton-Polyester Blend",
                "Denim",
                "Knitted Fabric"
            ]
        )

        working_hours = st.slider(
            "Working Hours Per Day",
            min_value=4,
            max_value=24,
            value=8
        )

    # Calculations
    gross_required = order_meters / (
        1 - waste_percent / 100
    )

    days_needed = gross_required / daily_capacity

    hourly_output = daily_capacity / working_hours

    st.subheader("Production Results")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Required Fabric",
        f"{order_meters:,.0f} m"
    )

    col2.metric(
        "Fabric Including Waste",
        f"{gross_required:,.0f} m"
    )

    col3.metric(
        "Production Time",
        f"{days_needed:.1f} days"
    )

    st.write(f"**Fabric Type:** {fabric_type}")

    st.write(
        f"**Hourly Production:** {hourly_output:.1f} meters/hour"
    )

    # Prepare report
    report = pd.DataFrame({
        "Item": [
            "Fabric Type",
            "Required Fabric",
            "Estimated Waste",
            "Gross Production Target",
            "Daily Capacity",
            "Production Days",
            "Working Hours Per Day"
        ],
        "Value": [
            fabric_type,
            f"{order_meters} meters",
            f"{waste_percent}%",
            f"{gross_required:.2f} meters",
            f"{daily_capacity} meters",
            f"{days_needed:.2f} days",
            working_hours
        ]
    })

    st.subheader("Production Report")

    st.dataframe(
        report,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        label="Download Production Report",
        data=report.to_csv(index=False).encode("utf-8"),
        file_name="textile_production_report.csv",
        mime="text/csv"
    )


# =========================
# FIBER GUIDE
# =========================

elif page == "Fiber Guide":

    st.markdown("""
    <div class="hero">
        <h1>Textile Fiber Guide</h1>
        <p>Learn about natural and man-made textile fibers.</p>
    </div>
    """, unsafe_allow_html=True)

    fibers = pd.DataFrame({
        "Fiber": [
            "Cotton",
            "Wool",
            "Silk",
            "Polyester",
            "Viscose",
            "Nylon",
            "Jute"
        ],

        "Classification": [
            "Natural - Plant",
            "Natural - Animal",
            "Natural - Animal",
            "Man-made - Synthetic",
            "Man-made - Regenerated",
            "Man-made - Synthetic",
            "Natural - Plant"
        ],

        "Properties": [
            "Soft, breathable, absorbent",
            "Warm, resilient, insulating",
            "Smooth, lustrous, lightweight",
            "Strong, quick-drying",
            "Soft and absorbent",
            "Strong and abrasion-resistant",
            "Coarse, strong, biodegradable"
        ],

        "Uses": [
            "Shirts, towels, denim",
            "Sweaters, coats, blankets",
            "Scarves, dresses",
            "Sportswear, uniforms",
            "Dresses and linings",
            "Activewear and hosiery",
            "Sacks, ropes, home products"
        ]
    })

    search = st.text_input(
        "Search Fibers",
        placeholder="Enter cotton, polyester, strong..."
    )

    if search:
        mask = fibers.astype(str).apply(
            lambda column: column.str.contains(
                search,
                case=False,
                na=False
            )
        ).any(axis=1)

        fibers = fibers[mask]

    st.dataframe(
        fibers,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Fiber properties depend on fiber quality, "
        "yarn construction, fabric structure, and finishing."
    )


# =========================
# ABOUT PAGE
# =========================

elif page == "About":

    st.markdown("""
    <div class="hero">
        <h1>About Textile Hub</h1>
        <p>A beginner-friendly textile industry application.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Textile Hub is a simple web application designed
    for textile engineering students and beginners.

    It provides basic information about textile production,
    fiber classification, and production planning.
    """)

    st.subheader("Application Features")

    st.markdown("""
    - Textile production dashboard
    - Production planning calculator
    - Fabric waste calculation
    - Textile fiber information
    - Downloadable production reports
    - Attractive user interface
    """)

    st.subheader("Technologies Used")

    st.markdown("""
    - Python
    - Streamlit
    - Pandas
    """)

    st.warning(
        "Dashboard values are sample data for demonstration. "
        "Use verified factory data for real production decisions."
    )


# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Textile Hub | Textile Industry Dashboard | Built with Streamlit"
)
