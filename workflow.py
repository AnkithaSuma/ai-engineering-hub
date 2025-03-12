def process(data):
    try:
        patient_name = data.get("patientName", "Unknown Patient")
        diagnosis = data.get("diagnosis", "No diagnosis provided")
        treatment = data.get("treatment", "No treatment specified")

        # If details are inside 'entry', extract them
        if "entry" in data and isinstance(data["entry"], list):
            for entry in data["entry"]:
                if isinstance(entry, dict):
                    patient_name = entry.get("patientName", patient_name) or patient_name
                    diagnosis = entry.get("diagnosis", diagnosis) or diagnosis
                    treatment = entry.get("treatment", treatment) or treatment

        return {
            "case_summary": f"Patient: {patient_name}\nDiagnosis: {diagnosis}\nTreatment: {treatment}"
        }
    
    except Exception as e:
        return {"error": f"Processing error: {str(e)}"}
