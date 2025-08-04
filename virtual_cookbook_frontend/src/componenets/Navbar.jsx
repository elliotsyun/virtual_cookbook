import { Link } from "react-router-dom";

export function Navbar() {

    return (
        <>
        <Link to="/">
            <button>
                Home
            </button>
        </Link>
        <Link to="/add_recipe">
            <button>
                Add Recipe
            </button>
        </Link>      
        <Link to="/category">
            <button>
                Categories
            </button>
        </Link>              
        </>
    )
}