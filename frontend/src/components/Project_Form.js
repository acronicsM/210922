import React from "react";

class BookForm extends React.Component{

    constructor(props) {
        super(props);
        this.state = {Project:[], text:'', }
    }


    handleChange(event){
        this.setState(
            {
                [event.target.name] : event.target.value
            }
        )
    }

    handleSubmit(event){
        console.log(this.state.login, this.state.password)
        this.props.get_token(this.state.login,this.state.password)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="login" placeholder="login"
                       value={this.state.login} onChange={(event) => this.handleChange(event)}/>
                <input type="password" name="password" placeholder="password"
                       value={this.state.password} onChange={(event) => this.handleChange(event)}/>
                <input type="submit" value="Login"/>
            </form>
        )

    }
}

export default LoginForm