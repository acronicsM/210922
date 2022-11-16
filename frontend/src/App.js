import Cookies from "universal-cookie";

import logo from './logo.svg';
import './App.css';
import React from 'react';
import axios from 'axios';
import UserList from './components/Users.js';
import ProjectList from './components/project.js';
import TodoList from './components/todo.js';
import ProjectTodo from './components/project_todo.js';
import NotFound404 from './components/NotFound404.js';
import LoginForm from './components/Auth.js';
import Menu from './components/Menu.js';
import TodoForm from './components/Todo_Form';


import {BrowserRouter, Route, Routes, Link, Navigate} from 'react-router-dom'

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'menu': [],
            'token': '',
        }
    }

    delete_project(id) {
        const headers = this.get_headers()
        axios.delete('http://127.0.0.1:8000/api/project/${id}', {headers}).then(response => {
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })

    }



    create_Todo(project, text, user) {
        console.log(project)
        const headers = this.get_headers()
        const data = {
            project: project[0],
            text: text,
            date_create: new Date,
            date_update: new Date,
            activ: true,
            user: user[0]
        }

        axios.post('http://127.0.0.1:8000/api/todo', data, {headers}).then(response => {
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })

    }

    delete_Todo(id) {
        const headers = this.get_headers()
        axios.delete('http://127.0.0.1:8000/api/todo/${id}', {headers}).then(response => {
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })

    }

    get_token(username, password) {
        const data = {username: username, password: password}
        axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный пароль или логин'))
    }

    set_token(token) {
        console.log(token)
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_auth() {
        return !!this.state.token
    }

    logout() {
        this.set_token('')
        this.setState({'authors': []}, () => this.load_data())
        this.setState({'books': []}, () => this.load_data())
    }

    get_headers() {
        let headers = {
            'Content-Type': 'applications/json'
        }
        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/user', {headers}).then(response => {
            this.setState({
                'users': response.data
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project', {headers}).then(response => {
            this.setState({
                'projects': response.data
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo', {headers}).then(response => {
            this.setState({
                'todos': response.data
            })
        }).catch(error => console.log(error))

    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li>
                            <Link to='/users'>Users</Link>
                        </li>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/todos'>Todos</Link>
                        </li>
                        <li>
                            {this.is_auth() ? <button onClick={() => this.logout()}>Logout </button> :
                                <Link to='/login'>Login</Link>}
                        </li>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<Navigate to='/projects'/>}/>
                        <Route path='/projects'>
                            <Route index element={<ProjectList projects={this.state.projects}
                                                               delete_project={(id) => this.delete_project(id)}/>}/>

                            <Route path=':projectId' element={<ProjectTodo todos={this.state.todos}/>}/>
                        </Route>

                        <Route exact path='/users' element={<UserList users={this.state.users}/>}/>

                        <Route exact path='/todos' element={<TodoList todos={this.state.todos}
                                                                      delete_Todo={(id) => this.delete_Todo(id)}/>}/>
                        <Route exact path='/todos/create'
                               element={<TodoForm projects={this.state.projects} users={this.state.users}
                                                  create_Todo={(projects, text, users) => this.create_Todo(projects, text, users)}/>}/>

                        <Route exact path='/login' element={<LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Route path='*' element={<NotFound404/>}/>
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
