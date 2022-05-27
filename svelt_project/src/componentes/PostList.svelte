<script>
    import { onMount } from 'svelte'
    
    const apiUrl = 'http://localhost:8000/api/v1/posts'
    let posts = []

    onMount(async() => {
        const response = await fetch(apiUrl)
        posts = await response.json()
        console.log(posts)
    })
</script>

{#each posts as post}
    <h3>{post.id}. {post.title}</h3>
    <p>{post.text}</p>
    <hr />
{/each}