import pandas as pd
import streamlit as st

df = pd.read_csv('users.csv')


st.title('Chargebee Customer Lookup')

# User input for chargebee_customer_id
chargebee_customer_id = st.text_input('Enter Chargebee Customer ID')

# Filter dataframe based on the input
if chargebee_customer_id:
    filtered_df = df[df['chargebee_customer_id'] == chargebee_customer_id]
    
    if not filtered_df.empty:
        # Select specific columns to display
        result_df = filtered_df[['Email', 'Email provider', 'Company name']]
        st.dataframe(result_df)

        # Get the common email provider from the results
        if not result_df.empty:
            common_email_provider = result_df['Email provider'].iloc[0]

            # Create a new dataframe for emails with different providers based on the filtered results
            different_provider_df = filtered_df[filtered_df['Email provider'] != common_email_provider]

            # Display the new dataframe
            st.subheader('Emails with Different Providers')
            st.dataframe(different_provider_df[['Email', 'Email provider', 'Company name']])
            
            # If no different providers, inform the user
            if different_provider_df.empty:
                st.write('No emails with different providers found.')
    else:
        st.write('No matching Chargebee Customer ID found.')
