import streamlit as st

def process(data):
    """Processes patient case data and returns structured summaries."""
    try:
        case_summaries = []

        if isinstance(data, dict) and isinstance(data.get("entry"), list):
            for entry in data["entry"]:
                if isinstance(entry, dict):
                    resource = entry.get("resource", {})

                    case_summaries.append({
                        "patient_name": resource.get("patientName", "Unknown Patient"),
                        "diagnosis": resource.get("diagnosis", "No diagnosis provided"),
                        "treatment": resource.get("treatment", "No treatment specified"),
                    })

        return {"cases": case_summaries}

    except Exception as e:
        return {"error": f"Processing error: {str(e)}"}

# Sample JSON data
data = {
    "entry": [
        {"resource": {"patientName": "John Doe", "diagnosis": "Fractured Arm", "treatment": "Cast and rest"}},
        {"resource": {"patientName": "Jane Smith", "diagnosis": "Migraine", "treatment": "Painkillers"}}
    ]
}

# Streamlit UI
st.title("Patient Case Summary")
st.write("This app processes patient records and summarizes key details.")

# Process and Display Results
result = process(data)
st.subheader("Case Summaries")
st.json(result)  # 📌 Structured display


import streamlit as st
st.write(process(data))  # ✅ Display result in Streamlit