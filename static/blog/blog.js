class ClickButton extends React.Component {
  state = {
    wasClicked: false
  }

  handleClick () {
    this.setState(
      {wasClicked: true}
    )
  }

  render () {
    let buttonText

    if (this.state.wasClicked)
      buttonText = 'Clicked!'
    else
      buttonText = 'Click Me'

    return <button
      className="btn btn-primary mt-2"
      onClick={
        () => {
          this.handleClick()
        }
      }
    >
      {buttonText}
    </button>
  }
}
class PostTable extends React.Component {

  render () {
    fetch(this.props.url)
    .then(response => response.json())
    .then(data => {
      // Use the parsed data here
      console.log(data);
    })
    return <div>test</div>
  }
}
const domContainer = document.getElementById('react_root')
ReactDOM.render(
  React.createElement(ClickButton),
  domContainer
)

ReactDOM.render(
  React.createElement(
    PostTable,
    {url: postListUrl}
  ),
  domContainer
)