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

//Temp
import foodPic from '../assets/DummyPhoto.jpg';

export default function RecipeDetailsScreen () {
  const token = localStorage.getItem('token');
  React.useEffect(() => { getDetails();}, [])
  const id = 1;
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
    } catch (err) {
      alert(err);
    }
  }

  const navigate = useNavigate();
  const stars = Array(5).fill(0);
  const [dishName, setDishName] = React.useState();
  const [duration, setDuration] = React.useState();
  const [pic, setPic] = React.useState();
  const [desc, setDesc] = React.useState();
  const [ingredients, setIngredients] = React.useState();
  const [currentValue, setCurrentValue] = React.useState(0);
  const [hoverValue, setHoverValue] = React.useState(undefined);
  const tag = ['Asian', 'Breakfast', 'Lunch', 'Dinner', 'NoviceLevel'];
  const steps = [
  'Heat the water to a boil, then add the noodles to 3/4 the level of ‘al dente’, after that lift and drain.',
  'Prepare non-stick pan, add a little cooking oil, sautée onion, shallots, red chili, garlic and sautée until they are half cooked.',
  'Add the drained noodles, sweet soy sauce, chili sauce, seasoningpowderand stir until smooth. ',
  'Add fried onions, stir again until smooth and cooked.'
  ]
  const [saved, setSaved] = React.useState(true);
  
  const handleClick = value => {
    setCurrentValue(value)
  }

  const handleMouseOver = newHoverValue => {
    setHoverValue(newHoverValue)
  };

  const handleMouseLeave = () => {
    setHoverValue(undefined)
  }
  
  return (
  <div className={styles.screen_container}>
    <NavigationBarHome style={{ alignSelf: 'start', position: 'absolute' }} isLogin={false}></NavigationBarHome>
    <h1 className={styles.title}> Indomie </h1>
    <span className={styles.info_container}> 
      <img src={Time} className={styles.duration}/> <span className={styles.duration_text}> 60 Mins </span> 
      <img src={Serving} className={styles.serving}/> <span className={styles.duration_text}> 6 Serving </span> 
    </span>
    <div className={styles.foodpic_container}> <img src={foodPic} className={styles.foodPic} alt='foodImage'/> </div> 
    <div className={styles.description_container}>
      <article className={styles.description}>
        <p> Master the classic Mie Goreng with this utterly moreish recipe! Mie Goreng is a classic noodle dish from Indonesia, Malaysia and Singapore.
        Noodles are cooked with prawns, chicken and vegetables to create a delicious noodle dish all topped with a sunny fried egg!
        This is a pushy recipe Dear Reader!</p>
      </article>
    </div>
    <div className={styles.filterTagContainer}>
      {tag.map((name, index)=> {
        return <FilterTagLabel name={name}> </FilterTagLabel>
      })}
    </div>
    {saved === false && <button className={styles.save_button} onClick={()=> setSaved(true)}> Save Recipe <img src={Unsaved} className={styles.saveIcon}/> </button>}
    {saved === true && <button className={styles.save_button} onClick={()=> setSaved(false)}> Saved Recipe <img src={Saved} className={styles.saveIcon}/> </button>}
    <div className={styles.main_conatiner}>
      <div className={styles.recipe_info}>
        <h2 className={styles.recipe_title}>Recipe By: </h2>
        <img src={Hat} className={styles.hat}/> <span className={styles.recipe_by}> Giovanni Pio </span> 
      </div>
      <div className={styles.ingredients_container}>
        <h2 className={styles.ingredients_title}> Ingredients: </h2>
        <div className={styles.ingredients_box}>
          <ul className={styles.ingredients_list}>
            <li>2 Indomie</li>
            <li>1 Egg</li>
            <li>3 Red Chilies</li>
            <li>5g Fried Shallots</li>
            <li>5g Cloves of Garlic</li>
            <li>3tbsp Sweet Soya Sauce </li>
            <li>25g Tomato</li>
          </ul>
        </div>
      </div>
    </div>
    <h2 className={styles.instruction}> Instructions: </h2>
    <ol className={styles.custom_list__numbered}>
      {steps.map((step, index) => {
        return <li><strong> {step} </strong><br/></li>
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
              onClick={() => handleClick(index + 1)}
              onMouseOver={() => handleMouseOver(index + 1)}
              onMouseLeave={handleMouseLeave}
              color={(hoverValue || currentValue) > index ? '#FFBA5A' : '#a9a9a9'}
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