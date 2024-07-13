import openai

def process_assignment(content):
    """Process the assignment content with ChatGPT to generate README.md."""
    openai.api_key = 'your-api-key-here'
    
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Generate a README.md file based on the following assignment instructions:\n\n{content}",
        max_tokens=1000
    )
    
    readme_content = response.choices[0].text.strip()
    return readme_content
