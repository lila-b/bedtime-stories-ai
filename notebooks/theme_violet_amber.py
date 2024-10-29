import gradio as gr

theme = gr.themes.Base(
    primary_hue="violet",
    secondary_hue="amber",
    radius_size="xxl",
).set(
    body_background_fill='*primary_200',
    body_background_fill_dark='*primary_950',
    body_text_color='*neutral_900',
    body_text_color_subdued='*neutral_600',
    background_fill_primary='*secondary_100',
    background_fill_primary_dark='*neutral_900',
    background_fill_secondary='*secondary_50',
    border_color_accent='*secondary_400',
    border_color_accent_dark='*secondary_600',
    border_color_accent_subdued='*secondary_500',
    border_color_primary='*secondary_500',
    border_color_primary_dark='*secondary_800',
    color_accent='*secondary_400',
    color_accent_soft='*secondary_200',
    checkbox_background_color='*secondary_50',
    checkbox_label_gap='*spacing_xl',
    input_background_fill='*secondary_50',
    input_background_fill_dark='*neutral_600',
    button_primary_background_fill='*primary_600',
    button_primary_background_fill_dark='*secondary_500',
    button_primary_background_fill_hover='*primary_800',
    button_primary_background_fill_hover_dark='*secondary_700',
    button_primary_border_color='*secondary_500',
    button_primary_border_color_hover='*secondary_100',
    button_primary_text_color_dark='black',
    button_primary_text_color_hover_dark='white',
    button_secondary_background_fill='*secondary_100',
    button_secondary_background_fill_hover='*secondary_200'
)

with gr.Blocks(theme=theme) as demo:
    ...