import React from 'react'
import styles from './styles/RecipeDashboard.module.css'
import RecipeContainer from './RecipeContainer'
import RecipeCard from './RecipeCard'

const RecipeDashboard = (props) => {
  let title = "Welcome to Dashboard";
  if (props.clickedButton === 'Saved') title = "Your Saved Recipes"
  if (props.clickedButton === 'Rated') title = "Recipes You Have Rated"
  if (props.clickedButton === 'Created') title = "Your Recipes"


  return (
    <div className={styles.container}>
        <div className={styles.title_container}> 
          <span className={styles.title}> {title} </span> 
        </div>
        <div className={styles.recipe_container}>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
          <RecipeCard styles={{minHeight: 0, minWidth:0}}></RecipeCard>
    
        </div>

    </div>
  )
}

export default RecipeDashboard