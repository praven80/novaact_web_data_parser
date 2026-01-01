import streamlit as st
import time
import os
import json
import re
from nova_act import NovaAct

# Simplified app layout
st.set_page_config(page_title="Nova Act Application")
st.title("Nova Act Application")

# API key handling
api_key = os.environ.get("NOVA_ACT_API_KEY", "")
if not api_key:
    api_key = st.text_input("Enter NovaAct API Key", type="password")
    if api_key:
        os.environ["NOVA_ACT_API_KEY"] = api_key

# Website URL
website_url = st.text_input(
    "Website URL"
)

# Instructions
instructions = st.text_area(
    "Instructions",
    height=100
)

# JSON Structure
json_structure = st.text_area(
    "JSON Structure",
    height=150
)

# Headless option
headless = st.checkbox("Run Headless", value=False)

# Create execute button
execute_button = st.button("Extract Data", type="primary", disabled=(not api_key or not website_url))

# Status container
status = st.empty()

def extract_data_from_website(client, url, user_instructions, json_template):
    """Extract data from website based on instructions and template"""
    status.info(f"Navigating to website: {url}")
    
    # Navigate to the website
    client.page.goto(url)
    client.page.wait_for_load_state("networkidle")
    
    # Create instruction
    extraction_instruction = f"""
    Visit this website and {user_instructions}
    
    Extract the data and format it according to this exact JSON structure:
    {json_template}
    
    Output only the JSON object, nothing else.
    """
    
    # Extract data
    status.info("Extracting data...")
    result = client.act(extraction_instruction, schema={"type": "object"})
    
    # Process result
    if hasattr(result, 'parsed_response') and result.parsed_response:
        return result.parsed_response
        
    # Try to parse text response
    if hasattr(result, 'text'):
        text = result.text
        
        # Clean up text and try to parse as JSON
        text = re.sub(r'^.*?(\{)', r'\1', text, flags=re.DOTALL)
        text = re.sub(r';\\$', '', text)
        
        try:
            return json.loads(text)
        except:
            # Try to find JSON in the response
            json_pattern = r'(\{[\s\S]*\}|\$\$[\s\S]*\$\$)'
            matches = re.search(json_pattern, text)
            if matches:
                try:
                    json_str = matches.group(1).replace('\\"', '"').replace('\\\\', '\\')
                    return json.loads(json_str)
                except:
                    pass
    
    # Fallback to template
    try:
        return json.loads(json_template)
    except:
        return {"extraction_failed": True}

if execute_button:
    client = None
    
    try:
        with st.spinner("Working..."):
            # Initialize and start NovaAct
            client = NovaAct(
                starting_page="https://www.google.com",
                nova_act_api_key=api_key,
                headless=headless,
                chrome_channel="chromium"
            )
            client.start()
            
            # Extract data
            extracted_data = extract_data_from_website(
                client, website_url, instructions, json_structure
            )
            
            # Display results
            if extracted_data:
                # Clear status message
                status.empty()
                
                # Display as verbose text
                st.subheader("Detailed Analysis")
                
                # Display as JSON
                st.subheader("Raw JSON Data")
                st.json(extracted_data)
                
                # Add download button
                st.download_button(
                    label="Download JSON",
                    data=json.dumps(extracted_data, indent=2),
                    file_name="data.json",
                    mime="application/json"
                )
            else:
                st.error("Failed to extract data")
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
    
    finally:
        # Clean up
        if client:
            try:
                client.stop()
            except:
                pass