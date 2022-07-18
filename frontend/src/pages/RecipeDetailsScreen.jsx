import React from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { APICall } from '../helperFunc';
import NavigationBarHome from '../components/NavigationBarHome';
import FilterTagLabel from '../components/FilterTagLabel';
import styles from './styles/RecipeDetailsScreen.module.css';
import Time from '../assets/duration.svg'
import Serving from '../assets/serving.svg';
import Hat from '../assets/chef-hat.svg'
import Saved from '../assets/saved.svg'
import Unsaved from '../assets/unsaved.svg'
import Rating from '@mui/material/Rating';

export default function RecipeDetailsScreen () {
  const token = localStorage.getItem('token');
  const id = useParams();
  React.useEffect(() => { 
    let isFetch = true;
    getDetails();
    return () => isFetch = false;
    }, [id])
  
  const navigate = useNavigate();
  const [starsRating, setStarsRating] = React.useState(null);
  const [recipe, setRecipe] = React.useState({});
  const [tags, setTags] = React.useState([]);
  const [ingredients, setIngredients] = React.useState([]);
  const [steps, setSteps] = React.useState([]);
  const [avg_rating, setAvgRate] = React.useState(0);
  
  const getDetails = async () => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token': token,
      };
      const data = await APICall(null, `/recipe_details/view?id=${id}`, 'GET', headers);
      if (data.error) {
        throw new Error(data.error);
      }
      console.log(data);
      setRecipe(data);
      setTags(data.tags);
      setIngredients(data.ingredients);
      setSteps(data.steps);
      setAvgRate(data.avg_rating);
    } catch (err) {
      alert(err);
    }
  }

  const rateRecipe = async () => {
    try {
      const headers = {
        'Content-Type': 'application/json',
        'token': token,
      }
      const requestedBody = {
        rating: starsRating,
        recipe_id: recipe.recipe_id,
      }
      const data = await APICall(requestedBody, `/save_and_rate/rate`, 'POST', headers);
      if (data.error) {
        throw new Error(data.error);
      }
    } catch (err) {
      alert(err);
    }
  }
  
  const handleSave = async () => {
    try {
      const requestBody = {
        recipe_id: recipe.recipe_id,
      };
      const headers = {
        'Content-Type': 'application/json',
        'token': token,
      };
      await APICall(requestBody, '/save_and_rate/save', 'POST', headers);
      getDetails()
    } catch (err) {
      alert(err);
    }
  }
  
  return (
  <div className={styles.screen_container}>
    <NavigationBarHome style={{ alignSelf: 'start', position: 'absolute' }} isLogin={false}></NavigationBarHome>
    <h1 className={styles.title}> {recipe.title} </h1>
    <span className={styles.info_container}> 
      <img src={Time} className={styles.duration}/> <span className={styles.duration_text}> {recipe.time_required} Mins </span> 
      <img src={Serving} className={styles.serving}/> <span className={styles.duration_text}> {recipe.servings} Serving </span> 
    </span>
    <div className={styles.foodpic_container}> <img src={recipe.image} className={styles.foodPic} alt='foodImage'/> </div> 
    <div className={styles.description_container}>
      <article className={styles.description}>
        <p> {recipe.description} </p>
      </article>
    </div>
    <div className={styles.filterTagContainer}>
      {tags.map((list, index)=> {
        return <FilterTagLabel name={list.name}> </FilterTagLabel>
      })}
    </div>
    <div className={styles.icon_container}>
      {recipe.saved === false && <button className={styles.save_button} onClick={handleSave}> Save Recipe <img src={Unsaved} className={styles.saveIcon}/> </button>}
      {recipe.saved === true && <button className={styles.save_button} onClick={handleSave}> Save Recipe <img src={Saved} className={styles.saveIcon}/> </button>}
      <Rating name="half-rating" value={avg_rating} precision={0.5} size="large" sx={{ verticalAlign: '-10px', ml: '5px'}} readOnly/>
      <span> {avg_rating} </span>
    </div>
    <div className={styles.main_conatiner}>
      <div className={styles.recipe_info}>
        <h2 className={styles.recipe_title}>Recipe By: </h2>
        <img src={Hat} className={styles.hat}/> <span className={styles.recipe_by}> {recipe.author} </span> 
      </div>
      <div className={styles.ingredients_container}>
        <h2 className={styles.ingredients_title}> Ingredients: </h2>
        <div className={styles.ingredients_box}>
          <ul className={styles.ingredients_list}>
            {ingredients.map((list, index) => {
              return <li> {list.description} </li>
            })}
          </ul>
        </div>
      </div>
    </div>
    <h2 className={styles.instruction}> Instructions: </h2>
    <ol className={styles.custom_list__numbered}>
      {steps.map((list, index) => {
        return <li><strong> {list.description} </strong><br/></li>
      })}
    </ol>
    <div className={styles.rateContainer}>
      <h2> Leave a Rating! </h2>
      <div style={styles.stars}>
         <Rating 
          value={starsRating} 
          precision={1} 
          size="large" 
          sx={{ verticalAlign: '-10px', ml: '5px'}}
          onChange={(event, newValue) => {
            setStarsRating(newValue);
          }}
          />
      </div>
      <button className={styles.save_button} onClick={rateRecipe}>
        Submit
      </button>
    </div>
  </div>
  )
}