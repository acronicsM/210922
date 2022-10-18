import React from 'react';
import {useParams} from "react-router-dom";


const TodoItem = ({todo}) =>{
    return(
        <tr>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>
            <td>{todo.activ}</td>
            <td>{todo.user}</td>
        </tr>
    )
}

const ProjectTodo = ({todos}) =>{
    let {projectId} = useParams()
    console.log(projectId)
    console.log(todos)
    let filter_todos = todos.filter((todo)=> todo.project===(parseInt(projectId)))
    console.log(todos)
    return(
        <table>
            <th>Project</th>
            <th>text</th>
            <th>date_create</th>
            <th>date_update</th>
            <th>activ</th>
            <th>user</th>
            {filter_todos.map((todo_) => <TodoItem todo={todo_} />)}
        </table>
    )
}

export default ProjectTodo