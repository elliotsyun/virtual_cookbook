

export function RecipeList({ recipes, updateRecipe, updateCallback }) {    

    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_recipe/${id}`, options)
            if (response.status === 200) {
                updateCallback()
            } else {
                console.error("Failed to delete")
            }
        } catch (error) {
            alert(error)
        }
    }

    return <div>
        <h2>Recipes</h2>
        <table>
            <thead>
                <tr>
                    <th>Title</th>
                </tr>
            </thead>
            <tbody>
                {recipes.map((recipe) => (
                    // below we would put the recipe frame component
                    <tr key={recipe.id}>
                        <td>{recipe.title}</td>
                        <td>
                            <button onClick={() => updateRecipe(recipe)}>Update</button>
                            <button onClick={() => onDelete(recipe.id)}>Delete</button>
                        </td>
                        <td>
                            <div>
                                <img    
                                        // temporarily just display the image alongisde the buttons
                                        src={`http://127.0.0.1:5000${recipe.image}`} 
                                        alt={recipe.title}
                                        style={{ height: "100px" }}>
                                </img>
                            </div>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}