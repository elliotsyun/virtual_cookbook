import { useState } from "react";

const RecipeForm = ({ existingRecipe = {}, updateCallback }) => {
    const [title, setTitle] = useState(existingRecipe.title || "");

    // if an object is passed with AT LEAST 1 entry inside of it, then we're updating, otherwise we're creating
    const updating = Object.entries(existingRecipe).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            title,
        }
        const url = "http://127.0.0.1:5000/" + (updating ? `update_recipe/${existingRecipe.id}` : "create_recipe")
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="title">Title:</label>
                <input
                    type="text"
                    id="title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
            </div>
            <button type="submit">{updating ? "Update" : "Create"}</button>
        </form>
    );
};

export default RecipeForm