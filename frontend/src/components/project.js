import React from 'react';
import {Link} from 'react-router-dom';



const ProjectItem = ({project,delete_project}) =>{
    return(
        <tr>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name}</Link>
            </td>
            <td>{project.link}</td>
            <td>{project.users}</td>
             <td>
                <Link to={`/projects/${project.id}`}>task list</Link>
            </td>
            <td>
                <button onClick={()=>delete_project(project.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects,delete_project}) =>{
    return(
        <table>
            <th>Project name</th>
            <th>Link</th>
            <th>users</th>
            <th>todo</th>
            <th>actions</th>
            {projects.map((project_) => <ProjectItem project={project_} delete_project={delete_project}/>)}
        </table>
    )
}

export default ProjectList