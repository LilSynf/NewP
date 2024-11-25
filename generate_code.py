import openai
import os

# Set your OpenAI API key
openai.api_key = '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'

def generate_program(requirements, project_name):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a Python program based on the following requirements:\n{requirements}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500
    )
    code = response.choices[0].message['content'].strip()

    # Ensure the 'generated_programs' directory exists
    output_dir = os.path.join('app', 'generated_programs')
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, f"{project_name}.py")
    with open(file_path, 'w') as file:
        file.write(code)
    return file_path