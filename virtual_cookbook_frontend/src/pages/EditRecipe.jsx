import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { MultiField } from "../componenets/MultiField";

export function EditRecipe({currentRecipe, setCurrentRecipe}) {
    const [title, setTitle] = useState(currentRecipe.title)
    const [steps, setSteps] = useState(currentRecipe.steps || [""])
    const [ingredients, setIngredients] = useState(currentRecipe.ingredients || [""])
    const [tags, setTags] = useState(currentRecipe.tags || [""])

    const navigate = useNavigate();

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            title,
            steps,
            ingredients,
            tags,
        }
        const url = "http://127.0.0.1:5000/" + `update_recipe/${currentRecipe.id}`
        const options = {
            method: "PATCH",
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
            setCurrentRecipe("")
            navigate('/')
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

            <MultiField stateVar={steps} setter={setSteps} fieldUnit={"Step"}/>

            <MultiField stateVar={ingredients} setter={setIngredients} fieldUnit={"Ingredient"}/>
         
            <MultiField stateVar={tags} setter={setTags} fieldUnit={"Tag"}/>

            <button type="submit">Update</button>
        </form>
    )
}