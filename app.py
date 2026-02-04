{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO0WqCVjpoVSoue3vJEbCU8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/brad594/Concept_S8_App/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XKaoRYXhS19v",
        "outputId": "c7806bb9-6ada-45d7-94c8-6ac7d3f88550"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: google-generativeai in /usr/local/lib/python3.12/dist-packages (0.8.6)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (2.32.5)\n",
            "Requirement already satisfied: google-ai-generativelanguage==0.6.15 in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (0.6.15)\n",
            "Requirement already satisfied: google-api-core in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.29.0)\n",
            "Requirement already satisfied: google-api-python-client in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.188.0)\n",
            "Requirement already satisfied: google-auth>=2.15.0 in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.47.0)\n",
            "Requirement already satisfied: protobuf in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (5.29.5)\n",
            "Requirement already satisfied: pydantic in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (2.12.3)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (4.67.1)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.12/dist-packages (from google-generativeai) (4.15.0)\n",
            "Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in /usr/local/lib/python3.12/dist-packages (from google-ai-generativelanguage==0.6.15->google-generativeai) (1.27.0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests) (3.4.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests) (2026.1.4)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.56.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core->google-generativeai) (1.72.0)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.12/dist-packages (from google-auth>=2.15.0->google-generativeai) (0.4.2)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.12/dist-packages (from google-auth>=2.15.0->google-generativeai) (4.9.1)\n",
            "Requirement already satisfied: httplib2<1.0.0,>=0.19.0 in /usr/local/lib/python3.12/dist-packages (from google-api-python-client->google-generativeai) (0.31.2)\n",
            "Requirement already satisfied: google-auth-httplib2<1.0.0,>=0.2.0 in /usr/local/lib/python3.12/dist-packages (from google-api-python-client->google-generativeai) (0.3.0)\n",
            "Requirement already satisfied: uritemplate<5,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from google-api-python-client->google-generativeai) (4.2.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.12/dist-packages (from pydantic->google-generativeai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.41.4 in /usr/local/lib/python3.12/dist-packages (from pydantic->google-generativeai) (2.41.4)\n",
            "Requirement already satisfied: typing-inspection>=0.4.2 in /usr/local/lib/python3.12/dist-packages (from pydantic->google-generativeai) (0.4.2)\n",
            "Requirement already satisfied: grpcio<2.0.0,>=1.33.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai) (1.76.0)\n",
            "Requirement already satisfied: grpcio-status<2.0.0,>=1.33.2 in /usr/local/lib/python3.12/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai) (1.71.2)\n",
            "Requirement already satisfied: pyparsing<4,>=3.1 in /usr/local/lib/python3.12/dist-packages (from httplib2<1.0.0,>=0.19.0->google-api-python-client->google-generativeai) (3.3.2)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.6.1 in /usr/local/lib/python3.12/dist-packages (from pyasn1-modules>=0.2.1->google-auth>=2.15.0->google-generativeai) (0.6.2)\n"
          ]
        }
      ],
      "source": [
        "pip install -U google-generativeai requests"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import requests\n",
        "import google.generativeai as genai\n",
        "\n",
        "# Set up the mobile interface\n",
        "st.set_page_config(page_title=\"Concept Electrical\", page_icon=\"⚡\")\n",
        "\n",
        "# 1. LOAD SECRETS (We will set these in Streamlit later)\n",
        "S8_API_KEY = st.secrets[\"S8_API_KEY\"]\n",
        "GEMINI_KEY = st.secrets[\"GEMINI_KEY\"]\n",
        "\n",
        "# 2. DEFINE THE TOOLS\n",
        "def search_job(query: str):\n",
        "    url = \"https://api.servicem8.com/api_1.0/search.json\"\n",
        "    headers = {\"X-Api-Key\": S8_API_KEY}\n",
        "    r = requests.get(url, headers=headers, params={'q': query})\n",
        "    return r.json()\n",
        "\n",
        "def get_job_info(job_uuid: str):\n",
        "    url = f\"https://api.servicem8.com/api_1.0/job/{job_uuid}.json\"\n",
        "    headers = {\"X-Api-Key\": S8_API_KEY}\n",
        "    r = requests.get(url, headers=headers)\n",
        "    return r.json()\n",
        "\n",
        "# 3. CONFIGURE AI\n",
        "genai.configure(api_key=GEMINI_KEY)\n",
        "model = genai.GenerativeModel(\n",
        "    model_name='gemini-2.0-flash',\n",
        "    tools=[search_job, get_job_info]\n",
        ")\n",
        "\n",
        "# --- THE APP INTERFACE ---\n",
        "st.title(\"⚡ Concept Job Finder\")\n",
        "\n",
        "if \"chat\" not in st.session_state:\n",
        "    st.session_state.chat = model.start_chat(enable_automatic_function_calling=True)\n",
        "\n",
        "user_input = st.text_input(\"Ask me about a job or address:\", placeholder=\"e.g. Status of 3 Bullock Ct?\")\n",
        "\n",
        "if user_input:\n",
        "    with st.spinner('Checking ServiceM8...'):\n",
        "        response = st.session_state.chat.send_message(user_input)\n",
        "        st.markdown(response.text)\n",
        "\n",
        "st.divider()\n",
        "st.caption(\"Brad's Private Admin Tool v1.0\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1Lln36JNfors",
        "outputId": "0680631d-0c37-4e5a-e8bb-11102ba0be78"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "System updated to Gemini 2.5. Ready for the Bullock Ct check.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "response = chat.send_message(\"What is the status of the job at 3 bullock ct wodonga?\")\n",
        "print(response.text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 104
        },
        "id": "f7mOR0lZgCdP",
        "outputId": "0e3b2a3a-25cf-4bce-d082-701175a32e26"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "There are multiple jobs at 3 Bullock Ct Wodonga. Could you please specify which job you are referring to?\n",
            "*   **Job 9212**: \"Supply and install a NHP Mod 6 Plus 36 Pole Chassis board...\" - Status: Work Order\n",
            "*   **Job 9124**: \"Look at CCTV CAMERA THAT HAS FAILED Look at exit light above switchboard exit\" - Status: Work Order\n",
            "*   **Job 9075**: \"Power monitoring with Bryce from control tech\" - Status: Completed\n",
            "*   **Job 9035**: \"Look at the ducks\" - Status: Completed\n"
          ]
        }
      ]
    }
  ]
}