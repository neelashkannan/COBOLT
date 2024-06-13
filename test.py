import mesop as me
import mesop.labs as mel
import ollama

@me.stateclass
class State:
  name: str
  size: int
  mime_type: str
  contents: str
  prompt : str
  toggled: bool = False
  radio_value: str = "2"
  sidenav_open: bool

def on_click(e: me.ClickEvent):
  s = me.state(State)
  s.sidenav_open = not s.sidenav_open


SIDENAV_WIDTH = 200

@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/",
  title="Mesop Demo Chat",
  
)




def app():  
  
  state = me.state(State)
  with me.sidenav(
    opened=state.sidenav_open, style=me.Style(width=SIDENAV_WIDTH)
  ):
    me.text("Inside sidenav")

  with me.box(
    style=me.Style(
      margin=me.Margin(left=SIDENAV_WIDTH if state.sidenav_open else 0),
    ),
  ):
    with me.content_button(on_click=on_click):
      me.icon("menu")
      #me.markdown("Main content")

    mel.chat(transform, title="C.O.B.O.L.T - A.I By Robonium", bot_user="Cobolt")

  
  
  
   

def transform(input: str, history: list[mel.ChatMessage]):
    me.text("Horizontal radio options")
    
    if(prompt := input):
        stream = ollama.chat(
            model="demo2",
            messages=[{'role': 'user', 'content': prompt}],
            stream=True,
        )
        full_response = ""
        
        
          
  
        for chunk in stream:
            yield chunk['message']['content']  # concatenate each chunk to the existing text
            
def on_change(event: me.RadioChangeEvent):
  s = me.state(State)
  s.radio_value = event.value
@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/1",
)
def app():
  s = me.state(State)
  me.text("Horizontal radio options")
  me.radio(
    on_change=on_change,
    options=[
      me.RadioOption(label="Option 1", value="1"),
      me.RadioOption(label="Option 2", value="2"),
    ],
    value=s.radio_value,
  )
  me.text(text="Selected radio value: " + s.radio_value)
