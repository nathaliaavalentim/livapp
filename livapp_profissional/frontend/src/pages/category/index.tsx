import { FormEvent, useState } from "react";
import Head from "next/head";
import { Header } from "../../components/Header";
import style from "./styles.module.scss";
import { setupAPIClient } from "../../services/api";
import { toast } from "react-toastify";
import { canSSRAuth } from "../../utils/canSSRAuth";


export default function Category(){

    const [name, setName] = useState('');

    async function handleRegister(e: FormEvent){
        e.preventDefault();
        if(name === ''){
            return;
        }

        const apiClient = setupAPIClient(undefined);
        await apiClient.post('/category', {
            name: name
        })


        toast.success("Instituição cadastrada com sucesso.")
        setName('');
    }

    return(
        <>
            <Head><title>Nova Instituição</title></Head>
            <div>
                <Header/>
                <main className={style.container}>
                    <h1>Nova Instituição</h1>
                        <form className={style.form}  onSubmit={handleRegister}>
                            <input
                            type="text"
                            placeholder="Digite o nome da instituição"
                            className={style.input}
                            value={name}
                            onChange={(e)=> setName(e.target.value)}
                        
                            />

                            <button type="submit" className={style.buttonAdd}>
                                Cadastrar
                            </button>

                        </form>
                    
                </main>
            </div>
        </>
    )
}

export const getServerSideProps = canSSRAuth(async (context)=>{
    return{
        props:{}
    }
})