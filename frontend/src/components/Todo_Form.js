import React from "react";

class TodoForm extends React.Component {

    constructor(props) {
        super(props);
        this.state = {Project: [], text: '', user: []}
    }

    handleChange(event) {
        this.setState({
                [event.target.name]: event.target.value
            }
        )
    }

    handleProjectChange(event) {
      if (!event.target.selectedOptions) {
            this.setState({
                'projects': []
            })
            return;
        }
        let projects = []
        for(let i = 0; i < event.target.selectedOptions.length;i++){
            projects.push(event.target.selectedOptions.item(i).value)
        }
        this.setState(
            {'projects':projects}
        )
    }

     handleUserChange(event) {
      if (!event.target.selectedOptions) {
            this.setState({
                'users': []
            })
            return;
        }
        let users = []
        for(let i = 0; i < event.target.selectedOptions.length;i++){
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState(
            {'users':users}
        )
    }


    handleSubmit(event) {
        this.props.create_Todo(this.state.projects, this.state.text, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="text"></label>
                    <input type="text" name="text" placeholder="text"
                           value={this.state.text}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                <select name="project" multiple onChange={(event) => this.handleProjectChange(event)}>
                    {this.props.projects.map((item) => <option value={item.id}>{item.name}</option>)}
                </select>

                 <select name="user" multiple onChange={(event) => this.handleUserChange(event)}>
                    {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)}
                </select>

                <input type="submit" value="Save"/>
            </form>
        )

    }
}

export default TodoForm