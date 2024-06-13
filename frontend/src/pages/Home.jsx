import { useState, useEffect } from "react"
import Project from "../components/Project.jsx"
import api from "../django_main"
import "../styles/Home.css"
function Home(){
    const [projects, setProjects] = useState([]);
    const [content, setContent] = useState("");
    const [name, setName] = useState("");

    useEffect(() => {
        getProjects();
    }, []);

    const getProjects = () => {
        api
            .get("/main/projects/")
            .then((res) => res.data)
            .then((data) => {
                setProjects(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

     const deleteProject = (id) => {
        api
            .delete(`/main/projects/delete//${id}/`)
            .then((res) => {
                if (res.status === 204) alert("Project deleted!");
                else alert("Failed to delete note.");
                getProjects();
            })
            .catch((error) => alert(error));
    };
     const createProject = (e) => {
        e.preventDefault();
        api
            .post("/main/projects/", { name, content })
            .then((res) => {
                if (res.status === 201) alert("Project created!");
                else alert("Failed to make project.");
                getProjects();
            })
            .catch((err) => alert(err));
    };

      return (
        <div>
            <div>
                <h2>Projects</h2>
                 {projects.map((project) => (
                    <Project project={project} onDelete={deleteProject} key={project.id} />
                ))}
            </div>
            <h2>Create a Project</h2>
            <form onSubmit={createProject}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="name"
                    name="name"
                    required
                    onChange={(e) => setName(e.target.value)}
                    value={name}
                />
                <label htmlFor="content">Content:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                ></textarea>
                <br />
                <input type="submit" value="Submit"></input>
            </form>
        </div>
    );
}

export default Home