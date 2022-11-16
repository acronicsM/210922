import React from 'react';
import {useParams} from "react-router-dom";


const TodoItem = ({todo,delete_Todo}) =>{
    return(
        <tr>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.date_create}</td>
            <td>{todo.date_update}</td>
            <td>{todo.activ}</td>
            <td>{todo.user}</td>
             <td>
                <button onClick={()=>delete_Todo(todo.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ProjectTodo = ({todos,delete_Todo}) =>{
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
            {filter_todos.map((todo_) => <TodoItem todo={todo_} delete_Todo={delete_Todo}/>)}
        </table>
    )
}

export default ProjectTodo