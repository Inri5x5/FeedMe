import React from 'react'
import styles from './styles/RatingsField.module.css'

const RatingsField = (props) => {

  const createContent = () => {
    let content = [];
    content.push(
      <>
        <div className={styles["reviews__single_star_average"]}>
          <div className={styles["single_star_average__amount"]}> 5 star</div>
          <div className={styles["single_star_average__progress_bar"]}>
            <progress
              className={styles["progress_bar__data"]}
              max="100"
              value={(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["five star"] / props.statistic.stats["num ratings"] * 100 : 0}
            ></progress>
          </div>
          <div className={styles["single_star_average__percentage"]}>{(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["five star"] / props.statistic.stats["num ratings"] * 100 : 0}%</div>
        </div>
        <div className={styles["reviews__single_star_average"]}>
          <div className={styles["single_star_average__amount"]}> 4 star</div>
          <div className={styles["single_star_average__progress_bar"]}>
            <progress
              className={styles["progress_bar__data"]}
              max="100"
              value={(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["four star"] / props.statistic.stats["num ratings"] * 100 : 0}
            ></progress>
          </div>
          <div className={styles["single_star_average__percentage"]}>{(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["four star"] / props.statistic.stats["num ratings"] * 100 : 0}%</div>
        </div>
        <div className={styles["reviews__single_star_average"]}>
          <div className={styles["single_star_average__amount"]}> 3 star</div>
          <div className={styles["single_star_average__progress_bar"]}>
            <progress
              className={styles["progress_bar__data"]}
              max="100"
              value={(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["three star"] / props.statistic.stats["num ratings"] * 100 : 0}
            ></progress>
          </div>
          <div className={styles["single_star_average__percentage"]}>{(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["three star"] / props.statistic.stats["num ratings"] * 100 : 0}%</div>
        </div>
        <div className={styles["reviews__single_star_average"]}>
          <div className={styles["single_star_average__amount"]}> 2 star</div>
          <div className={styles["single_star_average__progress_bar"]}>
            <progress
              className={styles["progress_bar__data"]}
              max="100"
              value={(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["two star"] / props.statistic.stats["num ratings"] * 100 : 0}
            ></progress>
          </div>
          <div className={styles["single_star_average__percentage"]}>{(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["two star"] / props.statistic.stats["num ratings"] * 100 : 0}%</div>
        </div>
        <div className={styles["reviews__single_star_average"]}>
          <div className={styles["single_star_average__amount"]}> 1 star</div>
          <div className={styles["single_star_average__progress_bar"]}>
            <progress
              className={styles["progress_bar__data"]}
              max="100"
              value={(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["one star"] / props.statistic.stats["num ratings"] * 100 : 0}
            ></progress>
          </div>
          <div className={styles["single_star_average__percentage"]}>{(props.statistic.stats["num ratings"] !== 0) ? props.statistic.stats["one star"] / props.statistic.stats["num ratings"] * 100 : 0}%</div>
        </div>
      </>
      
    )
    return content;
  }
  return (
    <>
      <div className={styles["reviews"]}>
        <div className={styles["reviews__breakdown"]}>
          <div className={styles["reviews_breakdown__wrapper"]}>
            {createContent()}
          </div>
        </div>
      </div>
    </>
  )
}

export default RatingsField