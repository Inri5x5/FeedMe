import React from 'react';

import SearchBar from '../components/SearchBar';
import NavigationBarHome from '../components/NavigationBarHome';
import FilterContainer from '../components/FilterContainer';
import RecipeCard from '../components/RecipeCard';
import { APICall } from '../helperFunc';
import Loading from '../components/Loading';


const HomeScreen = () => {
  const [loading, setLoading] = React.useState(true)
  const [selectedIngredients, setSelectedIngredients] = React.useState([]);
  const [selectedTags, setSelectedTags] = React.useState([]);
  const [foundRecipes, setFoundRecipes] = React.useState([]);

  const asyncFetchRecipes = async() => {
    let temp_data = [];
    let data = []
    let ing_ids = []
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token' : localStorage.getItem('token') ? localStorage.getItem('token') : -1
      };
      if (selectedIngredients.length > 0) {
        for(let i = 0; i < selectedIngredients.length; i++) {
          ing_ids.push(selectedIngredients[i].i_id)
        }
        const requestBody = {
          "ingredients_id" : ing_ids,
        }

        const requestBody2 = {
          "ingredient_id_list" : ing_ids,
        }
        temp_data = await APICall(requestBody, '/search/recipes', 'POST', headers);
        await APICall(requestBody2, '/search/has_searched', 'POST', headers);

        for(let i = 0; i < temp_data.recipes.length; i++) {
          data.push({
            "recipe_id" : temp_data.recipes[i].recipe_id,
            "recipe_name": temp_data.recipes[i].title,
            "recipe_desc": temp_data.recipes[i].description,
            "recipe_time": temp_data.recipes[i].time_required,
            "is_liked": temp_data.recipes[i].saved,
            "recipe_ratings": temp_data.recipes[i].avg_rating,
            "recipe_tags": temp_data.recipes[i].tags,
            "recipe_image": temp_data.recipes[i].image
          })
        }
        if (selectedTags.length > 0) {
          let result = []
          let tempIncludedTagId = []
          let tempExcludedTagId = []

          for (let i = 0; i < selectedTags.length; i++) {
            if (selectedTags[i].status === 'include') {
              tempIncludedTagId.push(selectedTags[i].tag_id)
            } else if (selectedTags[i].status === 'exclude') {
              tempExcludedTagId.push(selectedTags[i].tag_id)
            }
          }
          for (let i = 0; i < data.length; i++) {
            let tempAvailableTagId = []
            for (let j = 0; j < data[i].recipe_tags.length; j++) {
              tempAvailableTagId.push(data[i].recipe_tags[j].tag_id)
            }
            let validIncludedRecipe = tempIncludedTagId.every(tag_id => tempAvailableTagId.includes(tag_id))
            if (!validIncludedRecipe) continue
            let validExcludedRecipe = tempExcludedTagId.every(tag_id => !tempAvailableTagId.includes(tag_id))
            if (validExcludedRecipe) result.push(data[i])
    
          }
          setFoundRecipes(result)
        } else {
          setFoundRecipes(data)
        }
      }
    } catch (err) {
      alert(err);
    }
  }

  React.useEffect(() => {
    if (loading != true) {
      let tempTags = []
      let tempIngre = []
      if (localStorage.getItem('fm-ingredients')) {
        tempIngre = JSON.parse(localStorage.getItem('fm-ingredients'))
        setSelectedIngredients(tempIngre)
      }
      if (localStorage.getItem('fm-tags')) {
        tempTags = JSON.parse(localStorage.getItem('fm-tags'))
        setSelectedTags(tempTags)
      }
    }
  },[loading])
  
  React.useEffect(() => {
    if(selectedIngredients.length > 0) {
      localStorage.setItem('fm-ingredients', JSON.stringify(selectedIngredients))
    }
    if(selectedIngredients.length === 0) {
      localStorage.removeItem('fm-ingredients')
    }
    asyncFetchRecipes()
  },[selectedIngredients])

  React.useEffect(() => {
    if(selectedTags.length > 0) {
      localStorage.setItem('fm-tags', JSON.stringify(selectedTags))
    }
    if(selectedTags.length === 0) {
      localStorage.removeItem('fm-tags')
    }
    asyncFetchRecipes()
  },[selectedTags])
  
  const renderRecipesCard = () => {
    let content = []
    for (let i = 0; i < foundRecipes.length; i++) {
      content.push(
        <RecipeCard object={foundRecipes[i]} isEditable={false} isDelete={false} handleAfterLike={asyncFetchRecipes}/>
      )
    }
    return content
  }


  return (
    <>
      {(loading) && <Loading close={() => {setLoading(false)}} isHome={true}></Loading>}
      {(!loading) && <div style={{display: 'flex', flexDirection: 'column', height: '100%',}} > 
        <NavigationBarHome style={{ alignSelf: 'start' }} ></NavigationBarHome>
        <SearchBar
          selectedIngredients={selectedIngredients}
          setSelectedIngredients={setSelectedIngredients}
          numRecipesFound={foundRecipes.length}
        />
        <FilterContainer
          selectedTags={selectedTags}
          setSelectedTags={setSelectedTags} 
        />
        {(selectedIngredients.length > 0) && <div style={{
          position: 'relative',
          display: 'flex',
          flexDirection: 'row',
          justifyContent: 'space-evenly',
          flexWrap: 'wrap',
          alignContent: 'flex-start',
          marginTop: '20px',
          marginLeft: '20px',
        }}>
          {renderRecipesCard()}
        </div>}
        { (selectedIngredients.length === 0) && <div style={{
          display: 'flex',
          height: 'auto',
          width: '100%',
          padding: '300px 0',
          justifyContent: 'center',
          fontSize: '3em',
          fontWeight: 'bold',
          fontFamily: 'Righteous',
          color: 'rgba(229, 148, 7, 0.58)' 
        }}>
          Put in Your Ingredients Above
        </div>}
        { (selectedIngredients.length > 0) && (foundRecipes.length === 0) && <div style={{
          display: 'flex',
          height: 'auto',
          width: '100%',
          padding: '150px 0',
          justifyContent: 'center',
          fontSize: '3em',
          fontWeight: 'bold',
          fontFamily: 'Righteous',
          color: 'rgba(229, 148, 7, 0.58)' 
        }}>
          No Recipes Found
        </div>}
      </div>}
    </>
  )
}
  
export default HomeScreen;