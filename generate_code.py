import openai
import os

# Set your OpenAI API key
openai.api_key = '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'

def generate_program(requirements, project_name):
    prompt = f"Generate a Python program based on the following requirements:\n{requirements}"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=500
    )
    code = response.choices[0].text.strip()

    file_path = os.path.join('generated_programs', f"{project_name}.py")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(code)
    return file_path