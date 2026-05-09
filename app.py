import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_agent(role, goal, context):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": f"Tu es {role}. Ton objectif : {goal}"},
            {"role": "user", "content": context}
        ]
    )
    return response.choices[0].message.content

st.title("🧠 UX Research Agent")
st.caption("Analyse automatique de verbatims utilisateurs via multi-agents")

verbatims_default = """L'app est trop lente au démarrage.
Le bouton de paiement est introuvable.
J'adore l'interface, très intuitive !
Impossible de modifier mon profil.
La recherche ne fonctionne pas bien.
Très bonne expérience globalement.
Le menu est confus et mal organisé.
Les notifications sont trop fréquentes.
Design moderne et agréable.
Le support client ne répond pas vite."""

verbatims = st.text_area("📝 Colle tes verbatims (un par ligne)", value=verbatims_default, height=200)

if st.button("🚀 Lancer l'analyse"):
    if not verbatims.strip():
        st.warning("Ajoute des verbatims d'abord !")
    else:
        with st.status("Les agents travaillent...", expanded=True) as status:

            st.write("🕵️ Agent 1 — Analyse des problèmes...")
            analyse = run_agent(
                role="Analyste UX expert",
                goal="Identifier les problèmes récurrents dans les retours utilisateurs",
                context=f"Voici les verbatims:\n{verbatims}"
            )

            st.write("📊 Agent 2 — Catégorisation...")
            categories = run_agent(
                role="Catégoriseur UX",
                goal="Classer les problèmes par thèmes: navigation, performance, design, support",
                context=f"Voici l'analyse:\n{analyse}"
            )

            st.write("✍️ Agent 3 — Rédaction du rapport...")
            rapport = run_agent(
                role="Rédacteur UX senior",
                goal="Générer un rapport UX structuré avec recommandations actionnables en markdown",
                context=f"Voici les catégories:\n{categories}"
            )

            status.update(label="✅ Analyse terminée !", state="complete")

        st.markdown("## 📊 Rapport UX")
        st.markdown(rapport)
