import streamlit as st
from openai import OpenAI
from openai import OpenAI

client = OpenAI(api_key='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')
import os

class GeneralSerialKillerPlotOutlineGenerator:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_plot_outline(self, outline_name, details, tokens):
        prompt = self.construct_prompt(outline_name, details)
        response = client.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=tokens)
        return response.choices[0].message.content.strip()

    def construct_prompt(self, outline_name, details):
        prompts = [
            "Describe the setting and initial scenario of the mystery set in a futuristic city on Mars and a haunting virtual world, ensuring it evokes an atmosphere of hidden secrets and underlying tension. Introduce the main characters in a way that hints at their dark histories and complex backgrounds. Connect these introductions with the atmosphere of the futuristic city and virtual world.",
            "Detail the subtle foreshadowing of a rising menace from the lab. Describe the circumstances and signs that hint at the impending danger, creating an atmosphere of suspense and anticipation. These events should directly follow the initial scenario and character introductions.",
            "Introduce key characters in depth, focusing on their dark histories and complex backgrounds. Provide subtle hints about their past experiences and the emotional and psychological scars they bring to the unfolding narrative. Show how these characters are impacted by the rising menace and how their secrets start to unravel.",
            "Outline early plot developments that create panic and foreboding among the protagonists. Include specific incidents that build tension, doubt, and misunderstanding among the characters. These developments should naturally follow the character introductions and the impact of the foreshadowed menace.",
            "Describe the planning and execution of a blood-curdling event that fundamentally changes the reader’s perception of the story. This event should reveal hidden aspects or threats, adding depth to the mysterious narrative.",
            "Provide key moments where bewilderment and perplexity build up. Detail how these moments complicate the investigation and deepen the mystery. These moments should connect to the previous events and suspicions.",
            "Ensure every action and plot point maintains the story's spooky atmosphere. Use settings and actions to enhance the atmosphere of intrigue and fear. The suspense should build logically from the clues and suspicions raised.",
            "Detail the crafting of linked narratives with misleading indications. Explain how these narratives create a rich tapestry of tension and relationships. The misleading indications should add complexity to the existing tension and suspicions.",
            "Describe the process of revealing indicators that lead to false figures. Explain how these revelations change the story's direction and deepen the characters' interactions. The process should follow from the previous clues and suspicions.",
            "Introduce further surprising turns that recontextualize the entire story and previous twists. These turns should add a new layer of suspense and surprise just when the story seems to have settled.",
            "Describe how the story evolves after the first significant event and sets the stage for further developments. Outline the new conflicts, character dynamics, and plot directions that emerge as a result of the first event.",
            "Outline the impact of several deceptive signs and unveilings on the characters and the storyline. How do these unveilings reframe the characters' relationships and speculative journeys?",
            "Conclude the story with an unveiling where the killer's identity is truly unpredictable. Detail how this final twist ties up the narrative threads and leaves a lasting impression on the reader. The final twist should follow logically from the climactic confrontation and previous twists."
        ]
        combined_prompts = ' '.join([f"{i+1}. {p}: {details[i] if i < len(details) else ''}" for i, p in enumerate(prompts)])
        return f"Develop the {outline_name} of the serial killer mystery with the following key points: {combined_prompts}"

    def get_twist_description(self, serial_numbers):
        twist_types = {
            1: "The local police inspector, seemingly diligent, is actually the serial killer.",
            2: "A close family member of one of the victims is revealed to be an accomplice.",
            3: "An apparent suicide is discovered to be a murder staged to mislead investigators.",
            4: "A key witness has been lying about their alibi.",
            5: "The murder weapon is an everyday object with a hidden deadly purpose.",
            6: "An accident is revealed to be a cleverly disguised murder.",
            7: "A presumed victim is found alive and involved in the conspiracy.",
            8: "A seemingly insignificant detail becomes crucial to solving the mystery.",
            9: "The real motive for the crimes is far more sinister than initially believed.",
            10: "The serial killings are a cover-up for a larger criminal operation.",
            11: "A character's true identity is revealed, changing the entire context of the investigation.",
            12: "A secret relationship between two characters is exposed, altering the course of the investigation.",
            13: "The murders are connected to a historical or cultural event specific to the setting.",
            14: "An overheard conversation provides a vital clue that was initially overlooked.",
            15: "The killer's identity is revealed through a psychological breakdown.",
            16: "A long-lost letter or diary entry surfaces, providing crucial information.",
            17: "A character fakes their own death to avoid suspicion.",
            18: "The latest victim was not the intended target, leading to a new line of inquiry.",
            19: "A double life led by one of the characters is uncovered.",
            20: "The final twist reveals that the crimes were committed out of misguided love or loyalty."
        }
        return ' and '.join([twist_types.get(num, "Unknown Twist Type") for num in serial_numbers])

    def generate_general_serial_killer_plot_outline(self, outline_details, twist_serials, tokens=2000):
        selected_twist_descriptions = self.get_twist_description(twist_serials)
        twist_integration_instruction = f"Integrate the following twists into the story: {selected_twist_descriptions}. Ensure each twist is woven uniquely into the plot, impacting the story's direction, character dynamics, setting, and atmosphere in a mysterious yet coherent manner consistent with previous plot points."
        if len(outline_details) > 9:
            outline_details[9] = twist_integration_instruction
        else:
            outline_details.append(twist_integration_instruction)
        return self.generate_plot_outline("General Serial Killer Plot", outline_details, tokens)

    def interconnect_narrative_points(self, outline):
        prompt = f"See this story outline:\n\n{outline}\n\nEnsure each narrative point references previous ones for continuity and coherence. Add any necessary transitions or connections."
        response = client.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000)
        return response.choices[0].message.content.strip()

    def expand_plot_outline(self, outline, tokens=3000):
        prompt = f"Expand the following plot outline into a detailed, coherent, and connected chapter-wise plan. Maintain all original details, adding supporting plot points, character developments, and setting descriptions as necessary. The outline should read like an interesting plan, avoiding abstract language:\n\n{outline}"
        response = client.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=tokens)
        return response.choices[0].message.content.strip()


# Example usage
outline_gen = GeneralSerialKillerPlotOutlineGenerator('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')

# Define your outline details here
outline_details = [
    "Outline the setting and initial scenario of the a Futuristic City on Mars, ensuring it evokes a Haunting Virtual World. Introduce at least five main characters in a way that hints at their hidden secrets and potential motives. Ensure the setting is isolated, adding to the virtual unease.",
    "In the early chapters, weave in subtle foreshadowing elements that hint at rising lab menace. These should include lab experiments, unknown occurrences, and unknown key objects. Show how these elements affect each of the characters differently.",
    "Detail the introduction of crucial characters, emphasizing their dark histories and hidden explanations. Provide subtle hints about their past experiences and the emotional and psychological scars they bring to the unfolding narrative. Ensure interactions that create suspicion and tension among them.",
    "Outline early plot developments that create panic and foreboding among protagonists. These should include moments of tension, mistrust, and misunderstanding that deepen the characters' involvement and fear. Include group dynamics and conflicts.",
    "Plan the first blood-curdling execution that will fundamentally change the reader’s perception of the story. This twist should reveal hidden aspects or threats, adding depth to the eerie narratives narrative. Show how this event affects the group's dynamics and increases panic.",
    "In the outline, indicate key moments designed to build bewilderment and perplexity. These connections should be central to the story and enhance the impact of the first execution. Introduce false leads and suspicious behavior from multiple characters.",
    "Ensure that each plot point and character action is consistent with the story’s spooky atmosphere. The groundwork for the first twist should be laid carefully to maintain authenticity and avoid jarring deviations. Show how characters' backstories and actions interweave.",
    "Create multiple intertwined subplots that build a rich tapestry of tension and relationships. These threads should converge in the first twist, revealing their deeper significance. Highlight linked narratives and misleading indications.",
    "Outline the pivotal scene or chapter where the first major speculative twist is revealed after decoding indicators left by false figures. Plan how this revelation changes the story's direction and deepens the characters' interactions. Show the characters' reactions and how it influences their actions.",
    "Introduce a second, tail-end twist that recontextualizes the entire story and the original twist after revealing further surprising turns of extra layer of dread. This second twist should add a new layer of suspense and surprise just when the story seems to have settled. Ensure it ties back to earlier foreshadowing and character actions.",
    "Describe how the story evolves after the first twist and sets the stage for the second, twisting after the first slaying with new contentions and plot arcs elements. Outline the new conflicts, character dynamics, and plot directions that emerge as a result of the first twist. Show how characters adapt or fall apart.",
    "Outline the impact of the second twist on the characters and the storyline. How does this twist reframe the characters' several deceptive signs in characters' progression and plot? Show the final unraveling of secrets and resolutions.",
    "Concluding with a Truly Shocking and Unpredictable Plot Twist tying together all loose ends: Conclude the story in a manner that the unpredictability of the killer's identity completely recontextualizes everything that has happened before and still ties together and in detail explains in few sentences everything. Introduce a plot twist with the killer's identity being truly unpredictable such that it not only surprises the reader but also forces them to rethink the entire narrative from a new perspective. This twist should tie up the narrative threads in an unexpected way, leaving a lasting impression and shock value."
]

# Choose your twist serials
selected_twist_serials = [11,18,19]  # Example with multiple twist types

# Placeholder for the text
text_placeholder = st.empty()

def update_text():
    # Generate the outline with the selected twists
    outline_description = outline_gen.generate_general_serial_killer_plot_outline(outline_details, selected_twist_serials)

    # Expand the outline into a more detailed, chapter-wise plan
    detailed_outline = outline_gen.expand_plot_outline(outline_description)
    text_placeholder.text(detailed_outline)




# Show title and description.
st.title("💬 Plot Gene by Abhay Vignesh")
st.write(
    "Human in the loop Plot generation and narration. "
    "Generate story, movie plots"
)

# Create a button in the  UI
if st.button("Step 1"):
    update_text()
