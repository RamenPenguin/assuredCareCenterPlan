import streamlit as st
import fitz
import base64

# ------------------------
# Data
# ------------------------
data = {
    "Allergic Reaction (Rx_______________)": {
        "Problems": ["Risk for adverse reaction r/t previous reaction to client's triggers", "Deficient knowledge", "Impaired spontaneous ventilation", "Ineffective airway clearance", "Decreased cardiac output"],
        "Interventions": ["ADC will avoid client's triggers", "All staffs will be educated on Sx of anaphylactic reaction", "RN will administer rescue medicine per order and provide appropriate interventions if client is symptomatic s/p exposure", "RN will provide education on signs and symptonms of allergic reaction and medication compliance"],
        "Goals": ["Client will have no chest pain events when at the ADC", "Client's chest pain will be well managed if medication is administered per order"]
    },
    "Angina (Rx_______________)": {
        "Problems": ["Acute pain r/t myocardial ischemia", "Anxiety r/t situational crisis", "Decreased cardiac output r/t myocardial ischemia", "Risk for decreased cardiac tissue perfusion", "Risk for unstable blood pressure"],
        "Interventions": ["RN will assess client's level of anxiety and physical reaction to anxiety", "RN will implement pain management intervention to achieve satisfactory level of comfort, such as administering client's rescue medicine per order", "RN will provide education on maintaining heart healthy lifestyle", "RN will monitor client's VS on a regular basis", "RN will assess client's ability to tolerate ADL while at the ADC"],
        "Goals": ["Client will have no chest pain events when at the ADC", "Client's chest pain will be well managed if medication is administered per order"]
    },
    "Shortness of Breath (Rx_______________)": {
        "Problems" : ["Decreased activity tolerance", "Impaired gas exchange", "Anxiety r/t inability to breathe effectively, fear of suffocation", "Impaired spontaneous ventilation", "Ineffective airway clearance", "Ineffective breathing pattern"],
        "Interventions": ["RN will monitor client’s respiratory status and VS", "RN will administer client’s rescue medication per order with Sx", "The ADC will transfer client to the nearest ETC if client exhibited life threatening Sx such as inability to breath and hemodynamic instability", "RN will assess client’s level of anxiety and physical reaction to anxiety"],
        "Goals": ["Client will remain free from respiratory distress while at the ADC", "Client will be hemodynamically stable and return to baseline s/p treatment", "Client’s anxiety level will be well managed at the ADC", "Client will tolerated activities at the ADC"]
    },
    "Dementia": {
        "Problems" : ["Impaired memory r/t brain injury/ neurological impairment/ cognitive impairment", "Disturbed sensory perception", "Self-care deficit", "Social isolation r/t cognitive impairment"],
        "Interventions": ["RN will orient client to the environment as needed", "Staffs will encourage client to perform exercise, increase exposure to light", "Staffs will provide client with activities that enhance memory retention such as playing cards and socialization", "Staffs will aid with activities as needed while at the ADC", "Staffs will encourage social activities with the client’s peers"],
        "Goals" : ["Patient will demonstrate techniques to help improve memory impairment", "Patient will display improved memory through daily activities and interactions", "Patient will verbalize understanding of the importance of asking for assistance with activities as needed", "Patient will remain oriented while at the ADC"]
    },
    "Hypertension": {
        "Problems" : ["Risk for unstable blood pressure", "Risk for decreased cardiac output", "Deficient knowledge", "Excess fluid volume", "Sedentary lifestyle"],
        "Interventions" : ["RN will review client’s current medications and ensure that the list remains updated", "RN will educate client on the importance of medication compliance", "RN will monitor client’s VS regularly at the ADC", "Client will be encouraged to be actively involved with activities at the ADC", "RN will assess client’s fluid status as needed"],
        "Goals" : ["Client will maintained VS within normal range", "Client will remain asymptomatic with cardiac rhythm (absence of arrhythmia, tachycardia or bradycardia)", "Client will be free from dizziness with changes in positions", "Client will be free from generalized edema and respiratory distress", "Client will verbalize understanding of medication compliance and Sx of hemodynamic instability"]
    },
    "Diabetes" : {
        "Problems" : ["Risk for for unstable blood glucose level", "Ineffective health maintenance behaviors r/t complexity of therapeutic regimen", "Knowledge deficit", "Risk for infection", "Risk for impaired skin integrity", "Fatigue", "Imbalance nutrition", "Risk for disturbed","sensory perception"],
        "Interventions" : ["RN will review client’s current medication and updated as needed", "RN will monitor client’s blood glucose level frequently", "RN will educate client on medication compliance and healthy lifestyle", "RN will assess the development of skin ulcers", "RN will educate client on the importance of maintaining intact skin", "The ADC will provide low glycemic food for the client"],
        "Goals" : ["Client will maintain pre-prandial blood glucose of 90-150 mg/dL with chronic illness or 100-180 mg/dL with end-stage chronic illness", "Client will be compliant with her current diabetic medication regimen", "Client will be free from for signs and symptoms of Hypoglycemia/Hyperglycemia", "Client will remain free from infection", "Client skin will remain intact without ulcers", "Client will maintain healthy body weight", "Client will verbalize understanding of medication compliance and healthy lifestyle"]
    },
    "Fall Risk Intervention" : {
        "Problems" : ["musculoskeletal pain", "impaired physical mobility", "decreased lower extremities strength", "confusion", "cognitive dysfunction", "Slower reflexes"],
        "Interventions" : ["RN will complete fall risk assessment for older adults", "RN will evaluate client's medications to determine whether medications increase the risk of falling", "RN will screen all clients for balance and mobility skills", "RN will orient clients to the environment at the ADC", "All staff will provide ongoing supervision and assistance with activity"],
        "Goals" : ["Client will verbalize understanding of safe ambulation while at the ADC", "Client will remain free from fall incidents at the ADC", "Client will remain oriented while at the ADC", "Client will demonstrate safe use of assistive device for ambulation as needed (walker, wheelchair, cane)"]
    },
    "Hepatitis B" : {
        "Problems" : ["Decreased activity tolerance r/t weakness or fatigue caused by infection", "Acute pain r/t edema of the liver, bile irritating skin", "Readiness for enhanced knowledge", "Acute confusion", "Ineffective breathing pattern", "Ineffective tissue perfusion", "Risk for impaired skin integrity"],
        "Interventions" : ["RN will educate client on Sx of liver failure (confusion, excessive bleeding, bloating, abdominal pain, nausea and vomiting, decrease appetite, weakness, jaundice)", "RN will monitor client’s energy level and VS regularly", "RN will educate client on medication compliance", "RN will assess client’s mental status regularly", "RN will assess client’s respiratory status and skin integrity"],
        "Goals" : ["Client will tolerate appropriate activities at the ADC", "Client will verbalize understanding of medication compliance", "Client will remain free from hospitalizations", "Client’s pain will remain tolerable", "Client will remain free from Sx of liver failure (confusion, excessive bleeding, bloating, abdominal pain, nausea and vomiting, decrease appetite, weakness, jaundice)", "Client will be free from respiratory distress"]
    },
    "Cancer" : {
        "Problems" : ["Decreased activity tolerance", "Anxiety", "Ineffective coping", "Risk for bleeding", "Knowledge deficit", "Impaired oral mucous membrane integrity", "Chronic pain", "Self-Care deficit"],
        "Interventions" : ["Staff will aid ADL activities as needed at ADC", "Staff will encourage client to verbalize thoughts and feelings", "Staff will encourage social activities with client's peers", "RN will educate client on importance of medication compliance", "RN will educate client on implementing oral care protocol (soft toothbrush, normal saline mouth rinses, and avoiding tobacco, alcohol, irritating foods, etc.)", "RN will monitor and document vital"],
        "Goals" : ["Client will tolerate ADL while at ADC", "Client will demonstrate oral hygiene knowledge and skills to maintain intact oral mucous membranes", "Client vitals will remain within normal range", "Client will report increase in psychological comfort", "Client will remain free of destructive behaviors towards self and others", "Client will verbalize understanding of disease and progress and management"]
    },
    "Chronic pain" : {
        "Problems" : ["Chronic pain r/t BMI above normal", "Chronic pain r/t fatigue/musculoskeeltal dysfunction", "Chronic pain r/t injury agent", "Chronic pain r/t psychological distress", "Chronic pain r/t physiological factor", "Chronic pain r/t ________"],
        "Interventions" : ["RN will perform client's pain assessment with VS on a regular basis", "RN will review and update pain management plan (pharmacological and non-pharmacological approaches)", "RN will monitor for signs of depression/anxiety", "All staffs will be made aware of client's need for supervision with ambulation"],
        "Goals" : ["Client will tolerate ADL while at the ADC", "Client will verbalize tolerable pain level while at the ADC", "Client will remain VSS", "Client will remain free from falls"]
    }
}

# ------------------------
# Helper function
# ------------------------
def wrap_text(text, fontname, fontsize, max_width, doc):
    """Wrap text to fit within a given width. Supports \n line breaks."""
    lines = []
    for paragraph in text.split('\n'):
        words = paragraph.split()
        line = ""
        for word in words:
            test_line = f"{line} {word}".strip()
            width = fitz.get_text_length(test_line, fontname=fontname, fontsize=fontsize)
            if width <= max_width:
                line = test_line
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)
        lines.append("")
    return lines

def generate_pdf(topic, problems, interventions, goals):
    # Load template
    try:
        doc = fitz.open("assuredCareCenterPlan.pdf")
    except Exception as e:
        st.error(f"Error opening template PDF: {e}")
        return None

    page = doc[0]
    fontsize = 10
    fontname = "helv"

    page.insert_text((415, 75), f"{topic}", fontsize=12, fontname=fontname)
    lines = wrap_text("\n".join(problems), fontname, fontsize, 140, doc)
    page.insert_text((45, 175), lines, fontsize=fontsize, fontname=fontname)
    lines = wrap_text("\n".join(interventions), fontname, fontsize, 140, doc)
    page.insert_text((193, 175), lines, fontsize=fontsize, fontname=fontname)
    lines = wrap_text("\n".join(goals), fontname, fontsize, 205, doc)
    page.insert_text((346, 175), lines, fontsize=fontsize, fontname=fontname)

    # Save PDF into memory instead of file
    pdf_bytes = doc.write()
    doc.close()
    return pdf_bytes

pdf_link_container = st.empty()

def show_pdf(pdf_bytes, filename="output.pdf"):
    """
    Show a single download button for the generated PDF.
    """
    pdf_button_container.download_button(
        label="⬇️ Download PDF",
        data=pdf_bytes,
        file_name=filename,
        mime="application/pdf"
    )

st.title("Nursing Home Care Plan Generator")

topic = st.selectbox("Select a topic:", list(data.keys()))
if topic:
    st.subheader("Select Problems")
    problems = st.multiselect("Choose problems:", data[topic]["Problems"])

    st.subheader("Select Interventions")
    interventions = st.multiselect("Choose interventions:", data[topic]["Interventions"])

    st.subheader("Select Goals")
    goals = st.multiselect("Choose goals:", data[topic]["Goals"])

    if st.button("Generate PDF"):
        pdf_bytes = generate_pdf(topic, problems, interventions, goals)
        if pdf_bytes:
            st.success("PDF generated!")
            show_pdf(pdf_bytes)  # 👈 embedded preview
            st.download_button("Download PDF", data=pdf_bytes, file_name="output.pdf", mime="application/pdf")
