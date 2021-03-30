import Head from 'next/head'
import styles from '../styles/Home.module.css'
import data from './../database/data.json'

export default function Home({ allCountry }) {
  // const continentGetter = (subContinent) => {
  //   if (subContinent === "")
  // }
  return (
    <div>
      <Head>
        <title>All Country Details</title>
        <link rel="icon" type="image/png" href="https://freepikpsd.com/wp-content/uploads/2019/10/country-road-logo-png-6-Transparent-Images.png" />
      </Head>
      <h1 className={styles.headline}>All Country Details: </h1>
      <table className={styles.customers}>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Native Name</th>
          <th>Country Code</th>
          <th>Population</th>
          <th>Capital</th>
          <th>Continent</th>
          <th>TimeZones</th>
          <th>Area</th>
          <th>Flag</th>
        </tr>
        
       {allCountry.map((country, count) => (
         <tr>
          <td>{count+1}</td>
          <td>{country.name}</td>
          <td>{country.nativeName}</td>
          <td>{country.alpha3Code} {"-"} {country.alpha2Code}</td>
          <td>{country.population}</td>
          <td>{country.capital}</td>
          <td>{country.region}</td>
          <td>{country.timezones[0]}</td>
          <td>{country.area}</td>
          <td><img src={country.flag} height="25" width="25"></img></td>
         </tr>
       ))}
      </table>
    </div>
  )
}

export async function getStaticProps(context) {
  const res = await fetch(`https://restcountries.eu/rest/v2/all`)
  const allCountry = await res.json()
  // const allCountry = data;
  return {
    props: { allCountry },
  }
}
