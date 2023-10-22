import gradio as gr

theme = gr.themes.Soft().set(
    body_background_fill='none',
    body_background_fill_dark='none',
    body_text_weight='600',
    body_text_color_dark='*neutral_800',
    body_text_color_subdued='#666',
    body_text_color_subdued_dark='#666',
    background_fill_primary_dark='*neutral_50',
    background_fill_secondary_dark='*neutral_50',
    border_color_accent_dark='*neutral_300',
    border_color_primary_dark='*neutral_200',
    color_accent_soft_dark='*primary_50',
    link_text_color_dark='*secondary_600',
    link_text_color_active_dark='*secondary_600',
    link_text_color_hover_dark='*secondary_700',
    link_text_color_visited_dark='*secondary_500',
    shadow_spread_dark='6px',
    block_background_fill_dark='white',
    block_label_background_fill_dark='*primary_100',
    block_label_text_color_dark='*primary_500',
    block_title_text_color_dark='*primary_500',
    chatbot_code_background_color_dark='*neutral_100',
    checkbox_background_color_dark='*background_fill_primary',
    checkbox_background_color_selected_dark='*primary_600',
    checkbox_border_color_dark='*neutral_100',
    checkbox_border_color_focus_dark='*primary_500',
    checkbox_border_color_hover_dark='*neutral_300',
    checkbox_border_color_selected_dark='*primary_600',
    checkbox_border_width_dark='1px',
    checkbox_label_background_fill_selected_dark='*primary_500',
    checkbox_label_text_color_selected_dark='white',
    error_background_fill_dark='#fef2f2',
    error_border_color_dark='#b91c1c',
    error_text_color_dark='#b91c1c',
    error_icon_color_dark='#b91c1c',
    input_background_fill='*neutral_100',
    input_background_fill_dark='*neutral_100',
    input_background_fill_focus_dark='*secondary_500',
    input_border_color='*border_color_primary',
    input_border_color_focus_dark='*secondary_300',
    input_border_width='2px',
    input_border_width_dark='2px',
    input_placeholder_color_dark='*neutral_400',
    input_shadow='none',
    input_shadow_dark='none',
    input_shadow_focus='*input_shadow',
    input_shadow_focus_dark='*input_shadow',
    slider_color_dark='*primary_500',
    stat_background_fill_dark='*primary_300',
    table_border_color_dark='*neutral_300',
    table_even_background_fill_dark='white',
    table_odd_background_fill_dark='*neutral_50',
    button_primary_background_fill_dark='*primary_500',
    button_primary_background_fill_hover_dark='*primary_400',
    button_primary_border_color_dark='*primary_200',
    button_secondary_background_fill_dark='white',
    button_secondary_background_fill_hover_dark='*neutral_100',
    button_secondary_border_color_dark='*neutral_200',
    button_secondary_text_color_dark='*neutral_800'
)

css = """
body {background: url('file=images/background.jpg'); background-repeat: no-repeat; background-size: 100% auto; background-color: black;}
h1 {
    color: white !important}
.model3D .buttons {
    display: none !important}
.bubbletext {display: block;
  margin: 20px;
  padding: 10px;
  position: absolute;
  top: 20px;
  left: 10px;
  background: rgba(255, 255, 255, 0.8);
  width: 80%;
  border-radius: 10px 10px 10px 0px;
}
.attribution {
text-align: right;
  font-size: 10px !important;
  color: #444;
}
footer {
color: #ccc !important;
}
"""