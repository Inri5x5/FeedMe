import React from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBarHome from '../components/NavigationBarHome';
import UserDashboard from '../components/UserDashboard';
import RecipeContainer from '../components/RecipeContainer';

export default function UserProfileScreen2 () {
  const navigate = useNavigate();
  const [tabValue, setTabValue] = React.useState("Saved")
  
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
        <UserDashboard tabValue={tabValue} setTabValue={setTabValue}></UserDashboard>
        <RecipeContainer></RecipeContainer>
    
      </div>
    </>
  )
}