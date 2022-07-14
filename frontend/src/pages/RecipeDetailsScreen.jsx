import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';
import FilterTagLabel from '../components/FilterTagLabel';
import styles from './styles/RecipeDetailsScreen.module.css';
import Time from '../assets/duration.svg'
import Serving from '../assets/serving.svg';
import Hat from '../assets/chef-hat.svg'
//Temp
import foodPic from '../assets/DummyPhoto.jpg';

export default function RecipeDetailsScreen () {
  const navigate = useNavigate();
  
  const tag = ['Asian', 'Breakfast', 'Lunch', 'Dinner', 'NoviceLevel'];
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
    <button className={styles.save_button} onClick={()=> console.log('save')}> Save Recipe </button>
    <div className={styles.main_conatiner}>
      <div className={styles.recipe_info}>
        <h2 className={styles.recipe_title}>Recipe By: </h2>
        <img src={Hat} className={styles.hat}/> <span className={styles.recipe_by}> Giovanni Pio </span> 
      </div>
      <div className={styles.ingredients_container}>
        <h2 className={styles.ingredients_title}> Ingredients: </h2>
        <div className={styles.ingredients_box}>
          <ul className={styles.ingredients_list}>
            <li>2 Indomie </li>
            <li>1 Egg</li>
            <li>3 Red Chilies</li>
            <li>5g Fried Shallots </li>
            <li>5g Cloves of Garlic </li>
            <li>3tbsp Sweet Soya Sauce </li>
            <li>25g Tomato</li>
          </ul>
        </div>
      </div>
    </div>
    <h2> How To ? </h2>
    <ol className={styles.custom_list__numbered}>
      <li><strong>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</strong><br/>
      Nam fermentum orci ac justo facilisis, id imperdiet velit facilisis.</li>
      <li><strong>Praesent posuere tortor non diam commodo faucibus.</strong><br/>
      Donec id eros quis ipsum tempor mollis. Sed et sapien eu enim vulputate lobortis. Donec porttitor arcu at ante feugiat efficitur sed et lectus.</li>
      <li><strong>Vestibulum ac lectus nec lectus semper feugiat.</strong><br/>
      Vestibulum euismod lacus sit amet nisi dictum, sed sodales massa lobortis.</li>
      <li><strong>Donec ut ex eu urna facilisis fermentum ut vitae nulla.</strong></li>  
      <li><strong>Morbi at orci eu ligula congue sodales sed sed elit.</strong><br/>
      Donec ut quam ultrices, pharetra nibh ut, tristique lacus.</li>
      <li><strong>Proin in lectus ut ex tempor euismod.</strong><br/>
      Integer a arcu eleifend lorem consectetur malesuada nec ac massa. Integer imperdiet nisl eget consequat mollis. Vestibulum mollis lacus ac dui tempus lacinia.</li>
      <li><strong>Praesent facilisis nisl ut nisl lacinia scelerisque.</strong><br/>
      Curabitur rutrum dui ac urna semper ultrices.</li>
      <li><strong>Vestibulum tincidunt leo quis felis ullamcorper, varius suscipit massa iaculis.</strong></li>
      <li><strong>Curabitur mollis purus quis cursus ornare. Aenean dignissim quam et sem blandit ullamcorper.</strong><br />
      Nulla nec ante condimentum, tempor turpis et, vulputate ipsum. Fusce bibendum nunc et sagittis ornare. Proin aliquam odio ut enim porttitor egestas.</li>
      <li><strong>Pellentesque eleifend quam id scelerisque tincidunt.</strong></li>
    </ol>
  </div>
  )
}