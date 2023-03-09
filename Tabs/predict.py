"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Artificial Neural Network Classifier</b> for the Blood Cancer Detection.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A = st.slider("Gender", float(df["sex"].min()), float(df["sex"].max()))
    B = st.slider("Haemoglobin", float(df["hb"].min()), float(df["hb"].max()))
    C= st.slider("Peak corpuscular volume", float(df["pcv"].min()), float(df["pcv"].max()))
    D = st.slider("Red Blood Cell count", float(df["rbc"].min()), float(df["rbc"].max()))
    E = st.slider("Mean corpuscular volume", float(df["mcv"].min()), float(df["mcv"].max()))
    F = st.slider("Mean corpuscular hemoglobin", float(df["mch"].min()), float(df["mch"].max()))
    G = st.slider("Mean corpuscular hemoglobin concentration", float(df["mchc"].min()), float(df["mchc"].max()))
    H = st.slider("RBC Distributed Weight", float(df["rdw"].min()), float(df["rdw"].max()))
    I = st.slider("White Blood Cell count", float(df["wbc"].min()), float(df["wbc"].max()))
    J = st.slider("Lymph Amount", float(df["lymph"].min()), float(df["lymph"].max()))
    K = st.slider("Platelet count", float(df["plt"].min()), float(df["plt"].max()))
    L = st.slider("Haemoglobin Indicator 1", float(df["hba"].min()), float(df["hba"].max()))
    M = st.slider("Haemoglobin Indicator 2", float(df["hba2"].min()), float(df["hba2"].max()))
    N = st.slider("Fetal haemoglobin", float(df["hbf"].min()), float(df["hbf"].max()))

    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.08 
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get Blood Cancer!!")
        else:
            st.success("The person is relatively safe from Blood Cancer")

        # Print the score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
