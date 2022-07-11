import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';
import ContributorDashboard from '../components/ContributorDashboard';
import PublishedRecipeContainer from '../components/PublishedRecipeContainer';
import RecipeContainer from '../components/RecipeContainer'

export default function ContributorProfileScreen () {
  const navigate = useNavigate();
  const [tabValue, setTabValue] = React.useState("Published")
  
  React.useEffect(() => {
    //Fetch the recipe
    console.log(tabValue)
  }, [tabValue])
  
  return (
    <>
      <div style={{ 
        display:'flex',
        flexDirection:'column',
        height: '100%',
        alignItems:"center"
      }}>
        <NavigationBarHome style={{ alignSelf: 'start' }} isLogin={true} ></NavigationBarHome>
        <ContributorDashboard tabValue={tabValue} setTabValue={setTabValue}></ContributorDashboard>
        {(tabValue == 'Published') && <PublishedRecipeContainer></PublishedRecipeContainer>}
        {(tabValue == 'Drafted') && <RecipeContainer></RecipeContainer>}
      </div>
    </>
  )
}