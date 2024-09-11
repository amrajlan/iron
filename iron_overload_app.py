import streamlit as st

# Function to calculate LIC from T2* value
def calculate_lic(t2_star):
    return 30 / t2_star + 0.7

# Function to determine the severity of iron overload
def severity_of_iron_overload(lic):
    if lic <= 2:
        return "Normal"
    elif 2 < lic <= 7:
        return "Mild iron overload"
    elif 7 < lic <= 15:
        return "Moderate iron overload"
    else:
        return "Severe iron overload"

# Streamlit app UI
def main():
    st.title("Liver Iron Concentration (LIC) Calculator")
    
    # Input for T2* value
    t2_star = st.number_input("Enter T2* value (in ms)", min_value=0.1, step=0.1, value=14.1)
    
    # Calculate LIC
    if t2_star > 0:
        lic = calculate_lic(t2_star)
        conclusion = severity_of_iron_overload(lic)
        
        # Display the LIC and conclusion
        st.write(f"Liver Iron Concentration (LIC): {lic:.2f} mg/g dw")
        st.write(f"Conclusion: {conclusion}")
    else:
        st.write("Please enter a valid T2* value.")

if __name__ == '__main__':
    main()
