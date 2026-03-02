import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load variables from .env into environment
load_dotenv()

# ==========================================
# 1. CONFIGURATION
# ==========================================
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")
api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

# Validate config early (better error than a confusing API failure)
missing = [k for k, v in {
    "AZURE_OPENAI_ENDPOINT": endpoint,
    "AZURE_OPENAI_API_KEY": api_key,
    "AZURE_OPENAI_DEPLOYMENT": deployment_name,
}.items() if not v]

if missing:
    raise ValueError(f"Missing required .env values: {', '.join(missing)}")

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version=api_version,
)

# ==========================================
# 2. PROMPT LIBRARY
# ==========================================
def get_social_media_prompt(product, audience, tone):
    return f"""
Role: You are a viral social media manager.
Task: Write 3 catchy, short slogans for a product named "{product}".
Constraints:
- Target Audience: {audience}
- Tone: {tone}
- Max 10 words per slogan.
- Include one emoji per slogan.
"""

def get_corporate_prompt(product, audience, tone):
    return f"""
Role: You are a B2B Brand Strategist.
Task: Create 3 professional value propositions for "{product}".
Constraints:
- Target Audience: {audience}
- Tone: {tone} (Professional/Reliable)
- No emojis.
- Focus on efficiency and trust.
"""

# ==========================================
# 3. EXECUTION FUNCTION
# ==========================================
def run_generator(style, product, audience, tone):
    print(f"\n{'-' * 60}")
    print(f"🔹 GENERATING SLOGANS FOR: {product} ({style} style)")
    print(f"{'-' * 60}")

    if style == "social":
        prompt = get_social_media_prompt(product, audience, tone)
    else:
        prompt = get_corporate_prompt(product, audience, tone)

    print("\n[STEP 1] CONSTRUCTED PROMPT (Variable Injection):")
    print(prompt.strip())

    print("\n[STEP 2] CONNECTING TO AZURE...")
    try:
        response = client.chat.completions.create(
            model=deployment_name,  # Azure Deployment Name (from .env)
            messages=[
                {"role": "system", "content": "You are a helpful marketing assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7,
        )

        print("\n✅ SUCCESS! AI RESPONSE:")
        print(response.choices[0].message.content)

    except Exception as e:
        print("\n⚠️ API CALL FAILED")
        print(f"   Error Type: {type(e).__name__}")
        print(f"   Message: {e}")

# ==========================================
# 4. RUN TEST CASES
# ==========================================
if __name__ == "__main__":
    run_generator("social", "VoltRush Energy", "Gamers", "Exciting")
    run_generator("corporate", "IronClad Security", "CTOs", "Professional")