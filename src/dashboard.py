import streamlit as st
import pandas as pd

from agent import WaterIntakeAgent
from database import log_intake, get_intake_history


# ───────── Page Config ─────────
st.set_page_config(
    page_title="SipAI Dashboard",
    page_icon="💧",
    layout="wide"
)

# ───────── Profile Header ─────────
left, right = st.columns([7, 1])

with right:
    st.image("src/assets/pfp.jpg", width=70)
    st.markdown(
        "<p style='text-align:center; font-weight:600;'>CHARVI SINGH     </p>",
        unsafe_allow_html=True
    )

# ───────── Title ─────────
st.title("💧 AI Water Tracker Dashboard")

# ───────── Sidebar Input ─────────
st.sidebar.header("Log Your Water Intake")
user_id = st.sidebar.text_input("User ID", value="user_123")
intake_ml = st.sidebar.number_input(
    "Water Intake (ml)", min_value=0, step=100
)

if st.sidebar.button("Submit"):
    if user_id and intake_ml > 0:
        log_intake(user_id, intake_ml)
        st.success(f"✅ Logged {intake_ml} ml for {user_id}")

        agent = WaterIntakeAgent()
        feedback = agent.analyze_intake(intake_ml)
        st.info(f"🤖 AI Feedback:\n\n{feedback}")

# ───────── Divider ─────────
st.markdown("---")

# ───────── History Section ─────────
st.header("📊 Water Intake History")

history_container = st.container()

history = get_intake_history(user_id)

with history_container:
    if history:
        df = pd.DataFrame(
            history,
            columns=["Water Intake (ml)", "Date"]
        )

        df["Date"] = pd.to_datetime(df["Date"])

        # Show individual entries (NO aggregation)
        st.dataframe(
            df,
            use_container_width=True,
            height=300
        )

        st.line_chart(
            df,
            x="Date",
            y="Water Intake (ml)"
        )
    else:
        st.warning("⚠️ No water intake data found. Please log your intake first.")











# import streamlit as st
# import pandas as pd

# from agent import WaterIntakeAgent
# from database import log_intake, get_intake_history


# st.set_page_config(
#     page_title="SipAI Dashboard",
#     page_icon="💧",
#     layout="wide"
# )

# # Header
# left, right = st.columns([7, 1])
# with right:
#     st.image("src/assets/pfp.jpg", width=70)
#     st.markdown(
#         "<p style='text-align:center; font-weight:600;'>CHARVI SINGH</p>",
#         unsafe_allow_html=True
#     )

# st.title("💧 AI Water Tracker Dashboard")

# # Sidebar input
# st.sidebar.header("Log Your Water Intake")
# user_id = st.sidebar.text_input("User ID", value="user_123")
# intake_ml = st.sidebar.number_input("Water Intake (ml)", min_value=0, step=100)

# if st.sidebar.button("Submit"):
#     if user_id and intake_ml > 0:
#         log_intake(user_id, intake_ml)
#         st.success(f"✅ Logged {intake_ml} ml for {user_id}")

#         agent = WaterIntakeAgent()
#         feedback = agent.analyze_intake(intake_ml)
#         st.info(f"🤖 AI Feedback:\n\n{feedback}")

# st.markdown("---")
# st.header("📊 Water Intake History")

# history = get_intake_history(user_id)

# if history:
#     df = pd.DataFrame(history, columns=["Water Intake (ml)", "Date"])
#     df["Date"] = pd.to_datetime(df["Date"])

#     daily = df.groupby("Date").sum().reset_index()

#     st.dataframe(daily, use_container_width=True)
#     st.line_chart(daily, x="Date", y="Water Intake (ml)")
# else:
#     st.warning("⚠️ No water intake data found. Please log your intake first.")


# import streamlit as st
# import pandas as pd
# from datetime import datetime
# from agent import WaterIntakeAgent
# from database import log_intake, get_intake_history


# # Initialize session state
# if "tracker_started" not in st.session_state:
#     st.session_state.tracker_started = False


# # ───────────────── Welcome Screen ─────────────────
# if not st.session_state.tracker_started:
#     st.title("💧 SipAI — Your AI Hydration Assistant")
#     st.markdown("""
#     Track your daily hydration with the help of **SipAI**.  
#     Log your water intake, receive smart AI-powered insights,
#     and stay healthy effortlessly.
#     """)

#     if st.button("Start Tracking"):
#         st.session_state.tracker_started = True
#         st.experimental_rerun()


# # ───────────────── Dashboard ─────────────────
# else:
#     st.title("💧 AI Water Tracker Dashboard")

#     # Sidebar: Intake Input
#     st.sidebar.header("Log Your Water Intake")
#     user_id = st.sidebar.text_input("User ID", value="user_123")
#     intake_ml = st.sidebar.number_input(
#         "Water Intake (ml)", min_value=0, step=100
#     )

#     if st.sidebar.button("Submit"):
#         if user_id and intake_ml:
#             log_intake(user_id, intake_ml)
#             st.success(f"✅ Logged {intake_ml}ml for {user_id}")

#             agent = WaterIntakeAgent()
#             feedback = agent.analyze_intake(intake_ml)
#             st.info(f"🤖 AI Feedback: {feedback}")

#     # Divider
#     st.markdown("---")

#     # 📊 History Section
#     st.header("📊 Water Intake History")

#     if user_id:
#         history = get_intake_history(user_id)
#         if history:
#             dates = [
#                 datetime.strptime(row[1], "%Y-%m-%d")
#                 for row in history
#             ]
#             values = [row[0] for row in history]

#             df = pd.DataFrame({
#                 "Date": dates,
#                 "Water Intake (ml)": values
#             })

#             st.dataframe(df)
#             st.line_chart(df, x="Date", y="Water Intake (ml)")
#         else:
#             st.warning("⚠️ No water intake data found. Please log your intake first.")
