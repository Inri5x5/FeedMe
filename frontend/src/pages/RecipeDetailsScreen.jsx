import React from 'react';
import { useNavigate } from 'react-router-dom';
import { APICall } from '../helperFunc';
import NavigationBarHome from '../components/NavigationBarHome';
import FilterTagLabel from '../components/FilterTagLabel';
import styles from './styles/RecipeDetailsScreen.module.css';
import Time from '../assets/duration.svg'
import Serving from '../assets/serving.svg';
import Hat from '../assets/chef-hat.svg'
import Saved from '../assets/saved.svg'
import Unsaved from '../assets/unsaved.svg'
import { FaStar } from "react-icons/fa";
import Rating from '@mui/material/Rating';

export default function RecipeDetailsScreen () {
  const token = localStorage.getItem('token');
  const id = 0;
  React.useEffect(() => { 
    let isFetch = true;
    getDetails();
    return () => isFetch = false;
    }, [id])
  
  const navigate = useNavigate();
  const stars = Array(5).fill(0);
  const [starsRating, setStarsRating] = React.useState(0);
  const [hoverValue, setHoverValue] = React.useState(undefined);
  const [recipe, setRecipe] = React.useState({});
  const [tags, setTags] = React.useState([]);
  const [saved, setSaved] = React.useState();
  const [ingredients, setIngredients] = React.useState([]);
  const [steps, setSteps] = React.useState([]);
  const [avg_rating, setAvgRate] = React.useState(0);
  
  const getDetails = async () => {
    try {
      const headers = {
        'Content-Type': 'application/json',
      };
      const data = await APICall(null, `/recipe_details/view?id=${id}`, 'GET', headers);
      if (data.error) {
        throw new Error(data.error);
      }
      console.log(data);
      setRecipe(data);
      setTags(data.tags);
      setSaved(data.saved);
      setIngredients(data.ingredients);
      setSteps(data.steps);
      setAvgRate(data.avg_rating);
    } catch (err) {
      alert(err);
    }
  }
  
  const handleRating = value => {
    setStarsRating(value)
  }

  const handleMouseOver = newHoverValue => {
    setHoverValue(newHoverValue)
  };

  const handleMouseLeave = () => {
    setHoverValue(undefined)
  }
  
  const handleSave = async () => {
    console.log(token)
    try {
      const requestBody = {
        recipe_id: recipe.recipe_id,
      };
      const headers = {
        'Content-Type': 'application/json',
        'token': token,
      };
      await APICall(requestBody, '/save_and_rate/save', 'POST', headers);
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
      {saved === false && <button className={styles.save_button} onClick={handleSave}> Save Recipe <img src={Unsaved} className={styles.saveIcon}/> </button>}
      {saved === true && <button className={styles.save_button} onClick={()=> setSaved(false)}> Save Recipe <img src={Saved} className={styles.saveIcon}/> </button>}
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
              return <li> {list.decription} </li>
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
        {stars.map((_, index) => {
          return (
            <FaStar
              key={index}
              size={35}
              onClick={() => handleRating(index + 1)}
              onMouseOver={() => handleMouseOver(index + 1)}
              onMouseLeave= {handleMouseLeave}
              color={(hoverValue || starsRating) > index ? '#FFBA5A' : '#a9a9a9'}
              style={{
                marginRight: 10,
                cursor: "pointer"
              }}
            />
          )
        })}
      </div>
      <button className={styles.save_button}>
        Submit
      </button>
    </div>
  </div>
  )
}