import React from 'react';

import SearchBar from '../components/SearchBar';
import NavigationBarHome from '../components/NavigationBarHome';
import FilterContainer from '../components/FilterContainer';
import RecipeContainer from '../components/RecipeContainer';


const HomeScreen = () => {
    const [selectedIngredients, setSelectedIngredients] = React.useState([]);
    const [selectedTags, setSelectedTags] = React.useState([]);
    const [foundRecipes, setFoundRecipes] = React.useState([]);

    //Dummy Recipes Set Up
    let dummyRecipes = [];
    for (let i = 0; i < 15; i++) {
      dummyRecipes.push({"id": i, "image": null, "time_required": 100})
    }

    React.useEffect(() => {
      if (localStorage.getItem('fm-ingredients')) {
        setSelectedIngredients(JSON.parse(localStorage.getItem('fm-ingredients')))
      }
      if (localStorage.getItem('fm-tags')) {
        setSelectedTags(JSON.parse(localStorage.getItem('fm-tags')))
      }
      // Fetch the recipe based on the ingredients
      // Filter the recipe based on Tags
      // Set the Recipe
    },[])

    React.useEffect(() => {
      if(selectedIngredients.length > 0) {
        localStorage.setItem('fm-ingredients', JSON.stringify(selectedIngredients))
      }
      if(selectedIngredients.length === 0) {
        localStorage.removeItem('fm-ingredients')
      }
    },[selectedIngredients])
    React.useEffect(() => {
      if(selectedTags.length > 0) {
        localStorage.setItem('fm-tags', JSON.stringify(selectedTags))
      }
      if(selectedTags.length === 0) {
        localStorage.removeItem('fm-tags')
      }
    },[selectedTags])

    return (
      <>
        <div style={{display: 'flex', flexDirection: 'column'}} > 
          <NavigationBarHome style={{ alignSelf: 'start' }} ></NavigationBarHome>
          <SearchBar
            selectedIngredients={selectedIngredients}
            setSelectedIngredients={setSelectedIngredients}
          />
          <FilterContainer
            selectedTags={selectedTags}
            setSelectedTags={setSelectedTags} 
          />
          <RecipeContainer />
        </div>
      </>
    )
  }
  
export default HomeScreen;