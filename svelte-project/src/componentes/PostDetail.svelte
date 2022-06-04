<script>
    import { onMount } from 'svelte'
    
    export let params

    const apiUrl = 'http://localhost:8000/api/v1/posts/'
    let data = []

    onMount(async () => {
        const response = await fetch(apiUrl + params.id)
        data = await response.json()
    })
</script>

<h1>{data.title}</h1>
<p>{data.text}</p>