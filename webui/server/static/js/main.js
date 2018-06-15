async function api(url, opts = {}) {
    opts.credentials = opts.credentials || 'include'
    const resp = await fetch(url, opts)
    const dat = await resp.json()
    if (dat.status === 'ok') {
        return dat.data
    } else {
        throw new Error(dat.status)
    }
}
