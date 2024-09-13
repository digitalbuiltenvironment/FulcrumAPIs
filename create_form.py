import requests
import json
from dotenv import load_dotenv, set_key
import os

def create_form(extension_data):
    load_dotenv(override=True)

    # Base url currently points to PROD, can be changed
    base_url = "https://optimus.fulcrumhq.build"
    endpoint = "/api/services/app/Issues/CreateOrEdit"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Authorization": f"Bearer {os.getenv('ELEVATE_TOKEN')}",
        'Accept': 'text/plain',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Lt-Ou': '45', #change according to project
    }

    payload = {
        'issueDefinitionId': "349", # change according to project
        'extensionData': json.dumps(extension_data),  # JSON string for nested data
        'organizationUnitId': '45', # change according to project #same at Lt-Ou
        'sequenceType': 0,
        }    

    response = requests.post(base_url+endpoint, headers=headers, json=payload)
    print(response.status_code)
    if response.ok:
        print("Issue created or edited successfully.")
        print("Response code:", response.status_code)
        print("Response text:", response.text)
    else:
        print("Failed to create or edit issue.")
        print("Response code:", response.status_code)
        print("Response text:", response.text)    
    

    if response.status_code != 200:
        raise Exception(response.json()["error"]["message"])
    
    print("Form successful created")


# # how many times you wanna create the form?
# n = 5

# for i in range(n):

#     # Check if the user is signed in
#     response = requests.get(IS_SIGNEDIN_URL, headers=headers)

#     if response.ok:
#         print("User is signed in. Creating or editing issue...")
#         print("Response code:", response.status_code)
#         print("Response text:", response.text)

        # # payload for construction progress form
        # payload = {
        #     'issueDefinitionId': '199',
        #     'extensionData': "{\"workflow_\":\"1\",\"date_picker_F4E58E31-FE58-498E-8FB1-6F98FC5CAE57\":\"2024-02-18T16:00:00.000Z\",\"sectionbreak_C382C6C5-ECB3-4ACD-A1B0-FC17D8F59A55\":{\"shouldCompleteForm\":false,\"status\":\"2\"},\"dropdown_67D99BC6-E0C2-44BC-9C7E-E2CD598E60FC\":\"3\",\"dropdown_24922FBE52BF4BE3BE8D96621897F18D\":\"7\",\"text_input_EED1EA74-2DCB-49E1-9416-437A84962EE6\":\"1234\",\"dropdown_C7ED6055-1BBE-4358-96D2-E41EDC72F234\":\"7\",\"dropdown_submitter\":\"1\",\"form_link_8D751B5E-2233-447C-9E90-A95257C94FB0\":[],\"sectionbreak_9E6D412A-E38F-47D3-8D7D-8B6F39308BA4\":{\"shouldCompleteForm\":false,\"status\":\"0\"},\"checkboxes_F76F1DC8-0FC4-463D-96EF-08E15CFB2837\":[],\"text_input_240E4A62-3959-4BA7-A38E-20C2F56E5F8F\":\"\",\"sectionbreak_54393DB7-5748-4444-AF6A-59599297AE2A\":{\"shouldCompleteForm\":false,\"status\":\"0\"},\"text_input_3441E9E9-5AF5-44E6-9456-A25AE5F2D9F2\":\"\",\"text_input_FFC30DDF-A95D-4CA3-AE61-A056F1143057\":\"\",\"text_input_31F4FC4E9CB0497CBA1CA47CFB43E3D0\":\"\",\"text_input_0F9E36D7-4E24-4454-A5A7-E8A722C99E99\":\"\",\"dropdown_Status\":null,\"text_input_846CA160-89E9-4A60-B4DE-1F4E85E21CFD\":\"\",\"FileAttachments8DF00B08-5D1E-44A7-8F75-7D9310146A65\":[],\"text_input_6C3F9316-1F0D-4E08-A0EE-701DCF8BA8BF\":\"\",\"sectionbreak_3EC9C88D-1D8B-44D1-B3AA-BA9D71D5EF57\":{\"shouldCompleteForm\":false,\"status\":\"2\"},\"dropdown_4620E792-8F2C-43B8-8435-5E8F4C2E84C3\":\"1\",\"date_picker_7450B488-FC7D-4BA4-AC5E-554D57F1E6F4\":\"2024-02-18T16:00:00.000Z\",\"text_input_23519928-BB45-4EC9-86AC-350BA45BE43B\":\"\",\"sectionbreak_39F2154E-C927-425D-BF97-9A008949B775\":{\"shouldCompleteForm\":false,\"status\":\"2\"}}",
        #     # 'issueGuid': '8784868d-0528-4a3c-805a-45094425a9b5',
        #     'sequenceType': 0,
        #     'organisationUnitId': '28',
        # }

        # # payload for Contract Cashflow form in QAS
        # payload = {
        # 'issueDefinitionId': "226",
        # 'extensionData': "{\"sectionbreak_5FA6C46E-0960-4719-AF94-7CAAFF378ACF\":{\"shouldCompleteForm\":false,\"status\":\"2\"},\"dropdown_D8FF867E-57E9-4D68-9755-92E9D528F38A\":\"1\",\"dropdown_2377CE79-A01E-421C-9C5C-CC1811EC9E71\":\"1\",\"date_picker_17FEE9BA-676D-4733-8435-3FE2591333E1\":\"2024-04-22T16:00:00.000Z\",\"number_input_E0B2F44C-50E9-464C-9605-E7D0CD974E7E\":123,\"number_input_C02FD559-1DE2-4C6B-BEF8-E014B7B9B475\":1}",
        # # no need -> 'issueGuid': "8fe6d186-c6da-400c-889e-7579b574737e",
        # 'organizationUnitId': '33',
        # 'sequenceType': 0,
        # }

        # # payload for Contract Cashflow form in PROD
        # payload = {
        # 'issueDefinitionId': "349", # change according to project
        # 'extensionData': "{\"sectionbreak_5FA6C46E-0960-4719-AF94-7CAAFF378ACF\":{\"shouldCompleteForm\":false,\"status\":\"2\"},\"dropdown_D8FF867E-57E9-4D68-9755-92E9D528F38A\":\"1\",\"text_input_3B7F4EDB-1D02-42E0-8D7C-C86B97B685C2\":\"Build Only\",\"date_picker_17FEE9BA-676D-4733-8435-3FE2591333E1\":\"2021-07-31T16:00:00.000Z\",\"number_input_E0B2F44C-50E9-464C-9605-E7D0CD974E7E\":31861.85,\"number_input_C02FD559-1DE2-4C6B-BEF8-E014B7B9B475\":1}",
        # 'organizationUnitId': '45', # change according to project #same at Lt-Ou
        # 'sequenceType': 0,
        # }

    #     response = create_or_edit_issue(CREATE_EDIT_ISSUE_URL, headers, payload)

    #     if response.ok:
    #         print("Issue created or edited successfully.")
    #         print("Response code:", response.status_code)
    #         print("Response text:", response.text)
    #     else:
    #         print("Failed to create or edit issue.")
    #         print("Response code:", response.status_code)
    #         print("Response text:", response.text)
    # else:
    #     print("User is not signed in. Please sign in and try again.")
